import os
import re
import concurrent.futures
import json
import ast
import gc
import timeout_decorator
import sys
import gradio as gr
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from tqdm import tqdm
from src.utils.const import DIAGRAM_MAP, PATTERN

def _extract_python_function(response):
    """
    Extracts the Python function code and name from a model's response
    """
    try:
        match = re.search(PATTERN, response, re.DOTALL)
        if match:
            full_code = match.group(1).strip()
        else:
            print("Warning: No python code block found.")
            return response.strip(), False, ""

        tree = ast.parse(full_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_name = node.name
                function_code = ast.unparse(node)
                return function_code, True, function_name
        
        print("Warning: No function definition found in code block.")
        return None, False, ""
    except (SyntaxError, AttributeError) as e:
        print(f"Error parsing generated code: {e}")
        return None, False, ""

def _load_test(problem, test):
    """
    Load generated and official tests
    """
    tests = []
    path = f"problems/human_eval/{problem}/{test}.jsonl"
    
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            
            if isinstance(data[0]['input'], str):
                inputs = eval(data[0]['input'])
            else:
                inputs = data[0]['input']
            
            outputs = data[0]['output']

            for i in range(len(inputs)):
                tests.append((inputs[i], outputs[i]))
        return tests
    except FileNotFoundError:
        print(f"Error: Test file not found at {path}")
        return []
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
        print(f"Error loading or parsing test data from {path}: {e}")
        return []

def _run_code(code, tests, function_name, timeout = 5):
    """
    Run the provided test using the generated code
    """
    results = []

    @timeout_decorator.timeout(timeout, timeout_exception=TimeoutError)
    def execute_test(exec_code, local_vars):
        exec(exec_code, {}, local_vars)

    for case in tqdm(tests, desc="Running tests"):
        input_data = case[0]
        correct_output = case[1]

        if isinstance(input_data, tuple):
            exec_args = input_data
        else:
            exec_args = (input_data,)

        try:
            exec_code = f"{code}\nresult = {function_name}{repr(exec_args)}"
            local_vars = {}
            exec(exec_code, {}, local_vars)

            output = local_vars.get("result")

            if isinstance(output, bool):
                output = "Yes" if output else "No"

            success = output == correct_output
            error = ""
        except TimeoutError:
            success = False
            error = "Maximum time run reached"
            output = None
        except Exception as e:
            success = False
            error = str(e)
            output = None

        results.append({
            "success": success,
            "error": error,
            "input": input_data,
            "output": output,
            "correct_output": correct_output
        })

        del local_vars
        gc.collect()

    return results

def _process_task(args):
    problem, diagram, level, model_name = args
    diagram_folder = DIAGRAM_MAP.get(diagram)

    response_dir = os.path.join("results/human_eval", problem, model_name, diagram_folder)
    response_path = os.path.join(response_dir, f"l{level}_response.txt")

    try:
        with open(response_path, "r", encoding="utf-8") as f:
            response = f.read()
    except FileNotFoundError:
        return f"Warning: Response file not found for {problem}/{diagram}/L{level}"
    
    code, code_extracted, function_name = _extract_python_function(response)

    if code_extracted:
        code_path = os.path.join(response_dir, f"l{level}_code.py")
        os.makedirs(response_dir, exist_ok=True)
        with open(code_path, "w", encoding="utf-8") as f:
            f.write(code)
         
        official_tests = _load_test(problem, "official")
        generated_tests = _load_test(problem, "generated")
        
        official_results = _run_code(code, official_tests, function_name)
        generated_results = _run_code(code, generated_tests, function_name)
        
        official_path = os.path.join(response_dir, f"l{level}_official.jsonl")
        with open(official_path, 'w', encoding="utf-8") as f:
            for result in official_results:
                f.write(json.dumps(result) + '\n')

        generated_path = os.path.join(response_dir, f"l{level}_generated.jsonl")
        with open(generated_path, 'w', encoding="utf-8") as f:
            for result in generated_results:
                f.write(json.dumps(result) + '\n')
        
        return f"Success: Completed {problem}/{diagram}/L{level}"
    else:
        return f"Warning: No valid function found in {problem}/{diagram}/L{level}"
    
def run_bulk_code_test(model_name, problems, diagrams, levels):
    tasks = []
    
    filtered_diagrams = {}
    for diag in diagrams:
        if diag == "Block Diagram":
            filtered_diagrams[diag] = [lvl for lvl in levels if lvl == "1"]
        else:
            filtered_diagrams[diag] = levels
    
    for problem in problems:
        for diagram, level_list in filtered_diagrams.items():
            for level in level_list:
                tasks.append((problem, diagram, level, model_name))

    if not tasks:
        yield "No tests to run"
        return
    
    num_workers = max(1, os.cpu_count() - 2)

    print(f"Starting parallel execution with {num_workers} workers for {len(tasks)} tasks.")

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = list(tqdm(executor.map(_process_task, tasks), total = len(tasks), desc = "Running Bulk Test"))
    
    for result in results:
        if result.startswith("Warning"):
            yield result
            
    yield "Bulk test code completed."
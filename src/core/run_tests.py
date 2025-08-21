import os
import re
import json
import ast
import torch
import gc
import timeout_decorator
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PIL import Image
from tqdm import tqdm
from src.utils.const import DIAGRAM_MAP, PATTERN, MODEL_MAP, PROMPT
from src.core.model_manager import ModelManager


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
    
def _generate_response(model_manager, image, prompt):
    """
    Generate a response using the loaded model
    """
    try:
        return model_manager.generate_response(image, prompt)
    except Exception as e:
        print(f"Error generating response: {e}")
        return ""

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

    for case in tests:
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
    
def run_bulk_test(model_manager, problems, diagrams, levels, prompt):
    """
    Run bulk test for a selected model and problems:
    1. Filter block diagram to test only on level 1
    2a. Run test for each selected problem
    2b. Run test for each selected diagram
    2c. Run test for each selected level
    3a. Generate the response
    3b. Save the full response in a txt file
    4a. Extract the python generated function
    4b. Save the python generated function
    5. Load official and generated tests
    6a. Run the code
    6b. Save the results
    """

    print("AA")
    
    total_tests = len(problems) * len(diagrams) * len(levels)
    count = 0
    
    filtered_diagrams = {}
    for diag in diagrams:
        if diag == "Block Diagram":
            filtered_diagrams[diag] = [lvl for lvl in levels if lvl == "1"]
        else:
            filtered_diagrams[diag] = levels

    for problem in tqdm(problems, desc="Problems"):
        for diagram, level_list in filtered_diagrams.items():
            diagram_folder = DIAGRAM_MAP.get(diagram)
            
            for level in level_list:
                count += 1
                yield f"Problem: {problem}, Diagram: {diagram}, Level: {level} ({count}/{total_tests})"
                
                image_path = os.path.join("data/human_eval", problem, diagram_folder, f"l{level}.drawio.png")
                try:
                    image = Image.open(image_path)
                except FileNotFoundError:
                    yield f"Error: Image not found at {image_path}"
                    continue
                
                try:
                    response = _generate_response(model_manager, image, prompt)
                finally:
                    image.close()

                if not response:
                    yield "Error: Model response was empty."
                    continue

                response_dir = os.path.join("results/human_eval", problem, model_manager.model_name, diagram_folder)
                os.makedirs(response_dir, exist_ok=True)
                
                response_path = os.path.join(response_dir, f"l{level}_response.txt")
                with open(response_path, "w") as f:
                    f.write(response)

                code, code_extracted, function_name = _extract_python_function(response)

                if code_extracted:
                    code_path = os.path.join(response_dir, f"l{level}_code.py")
                    with open(code_path, "w") as f:
                        f.write(code)
                     
                    official_tests = _load_test(problem, "official")
                    generated_tests = _load_test(problem, "generated")

                    official_results = _run_code(code, official_tests, function_name)
                    generated_results = _run_code(code, generated_tests, function_name)

                    official_path = os.path.join(response_dir, f"l{level}_official.jsonl")
                    generated_path = os.path.join(response_dir, f"l{level}_generated.jsonl")
                    
                    with open(official_path, 'a') as f:
                        for result in official_results:
                            f.write(json.dumps(result) + '\n')

                    with open(generated_path, 'a') as f:
                        for result in generated_results:
                            f.write(json.dumps(result) + '\n')
                else:
                    yield "Warning: No valid function found in model response."
                
                torch.cuda.empty_cache()

    yield "Bulk test completed."

if __name__ == '__main__':
    problems = ["p084", "p106", "p108", "p119", "p120", "p126", "p131", "p147", "p150", "p155"]
    diagrams = ["bpmn", "fc"]
    levels = ["1", "2", "3"]

    models = list(MODEL_MAP.keys())

    for model in tqdm(models):
        print(f"Loading {model}")
        model_manager = ModelManager()
        model_manager.load_model(model)

        for problem in tqdm(problems):
            print(f"Test {problem}")
            run_bulk_test(model_manager, problem, diagrams, levels, PROMPT)

        for problem in tqdm(problems):
            print(f"Test {problem}")
            run_bulk_test(model_manager, problem, ["block"], ["1"], PROMPT)

        model_manager.unload_model()
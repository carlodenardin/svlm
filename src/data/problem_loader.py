import os
import json
import pandas as pd
from ast import literal_eval
import re

def _load_test_cases(file_path):
    """
    Load and normalize test cases from a JSONL file.
    Handles specific problems with string-formatted input/output.
    """
    tests = []
    problematic_problems = ["p120", "p150", "p155"]
    
    try:
        p_name = file_path.split('/')[-2]
    except IndexError:
        p_name = ""

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            raw_data = json.load(f)
            
            if isinstance(raw_data, list) and len(raw_data) > 0:
                item = raw_data[0]
                
                input_data = item.get('input', [])
                if p_name in problematic_problems and isinstance(input_data, str):
                    try:
                        input_data = literal_eval(input_data)
                    except (ValueError, SyntaxError) as e:
                        print(f"Error evaluating input string for {p_name}: {e}")
                        input_data = []
                
                if not isinstance(input_data, list):
                    input_data = []

                output_data = item.get('output', [])
                if p_name in problematic_problems and isinstance(output_data, str):
                    try:
                        output_data = literal_eval(output_data)
                    except (ValueError, SyntaxError) as e:
                        print(f"Error evaluating output string for {p_name}: {e}")
                        output_data = []

                if not isinstance(output_data, list):
                    output_data = []
                
                safe_len = min(len(input_data), len(output_data))
                
                for i in range(safe_len):
                    tests.append({"input": input_data[i], "output": output_data[i]})

    return tests

def _load_results(file_path):
    """
    Load results from a JSONL file.
    """
    results = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    results.append(json.loads(line.strip()))
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON line in {file_path}: {e}")
    return results

def _load_generated_code(file_path):
    """
    Load the generated Python code from a .py file.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read()
    return ""

def load_problem_data(problem):
    """
        Load all the dataset related to a specifc problem:
        1a. Load diagram paths (flowchart 3 levels, BPMN 3 levels, block 1 level)
        1b. Load test case (official and generated)
    """
    results_base_path = f"results/human_eval/{problem}"
    data = {}
        
    # 1a. Load Diagram paths
    data["FLOWCHART_PATHS"] = [f"data/human_eval/{problem}/fc/l{i}.drawio.png" for i in range(1, 4)]
    data["BPMN_PATHS"] = [f"data/human_eval/{problem}/bpmn/l{i}.drawio.png" for i in range(1, 4)]
    data["BLOCK_DIAGRAM_PATHS"] = [f"data/human_eval/{problem}/block/l1.drawio.png"]
    
    # 1b. Load test cases
    data["OFFICIAL_TESTS"] = _load_test_cases(f"problems/human_eval/{problem}/official.jsonl")
    data["GENERATED_TESTS"] = _load_test_cases(f"problems/human_eval/{problem}/generated.jsonl")
    
    # Load results and generated code for all models
    data["TEST_RESULTS"] = {}
    if os.path.exists(results_base_path):
        models = [d for d in os.listdir(results_base_path) if os.path.isdir(os.path.join(results_base_path, d))]
        for model in models:
            data["TEST_RESULTS"][model] = {}
            model_path = os.path.join(results_base_path, model)
            if os.path.exists(model_path):
                diagrams = [d for d in os.listdir(model_path) if os.path.isdir(os.path.join(model_path, d))]
                for diagram in diagrams:
                    data["TEST_RESULTS"][model][diagram] = {}
                    diagram_path = os.path.join(model_path, diagram)
                    if os.path.exists(diagram_path):
                        for filename in os.listdir(diagram_path):
                            match = re.search(r'^(l\d+)_(official|generated)\.jsonl$', filename)
                            if match:
                                level, test_type = match.groups()
                                file_path = os.path.join(diagram_path, filename)
                                results = _load_results(file_path)
                                if results:
                                    if level not in data["TEST_RESULTS"][model][diagram]:
                                        data["TEST_RESULTS"][model][diagram][level] = {}
                                    data["TEST_RESULTS"][model][diagram][level][test_type] = results
                            # Load generated code
                            if filename.startswith('l') and filename.endswith('.py'):
                                level = filename.split('.')[0]
                                code_path = os.path.join(diagram_path, filename)
                                code = _load_generated_code(code_path)
                                if code:
                                    if level not in data["TEST_RESULTS"][model][diagram]:
                                        data["TEST_RESULTS"][model][diagram][level] = {}
                                    data["TEST_RESULTS"][model][diagram][level]["code"] = code
    return data

def get_available_problems():
    problems_path = "problems/human_eval"
    if not os.path.exists(problems_path):
        return []
    problems = [d for d in os.listdir(problems_path) if os.path.isdir(os.path.join(problems_path, d))]
    problems.sort()
    return problems
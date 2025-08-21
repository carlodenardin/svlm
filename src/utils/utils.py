from ast import literal_eval
from src.utils.const import MODEL_MAP

import contextlib
import io
import json
import os
import pynvml as nvml
import re

def get_css_style():
    with open("src/ui/styles.css", "r") as f:
        style = f.read()
    
    return style

def get_gpu_info():
    nvml.nvmlInit()
    handle = nvml.nvmlDeviceGetHandleByIndex(0)
    name = nvml.nvmlDeviceGetName(handle)
    info = nvml.nvmlDeviceGetMemoryInfo(handle)
    total_mem_mib = info.total // (1024 * 1024)
    used_mem_mib = info.used // (1024 * 1024)
    
    return (
        f"```\n"
        f"Name: {name}\n"
        f"Memory: {used_mem_mib} MiB / {total_mem_mib} MiB\n"
        f"```"
    )

def run_python_code(code: str):
    stdout_capture = io.StringIO()
    with contextlib.redirect_stdout(stdout_capture):
        try:
            local_vars = {}
            exec(code, {}, local_vars)
            output = stdout_capture.getvalue()
        except Exception as e:
            output = f"An error occurred:\n{e}"
    return output

def update_link(model_name):
    if model_name and model_name in MODEL_MAP:
        model_id = MODEL_MAP[model_name]["model"]
        return f'<a href="https://huggingface.co/{model_id}" target="_blank" style="text-decoration: none;">https://huggingface.co/{model_id}</a>'
    return ""

def _load_test_cases(file_path):
    """
    Funzione ausiliaria per caricare e normalizzare i test da un file JSONL.
    Gestisce in modo specifico i problemi con l'input o l'output in formato stringa.
    """
    tests = []
    
    # List of problems that have input or output in string format
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
                
                input_data = []
                if 'input' in item:
                    input_data = item['input']
                    if p_name in problematic_problems and isinstance(input_data, str):
                        try:
                            input_data = literal_eval(input_data)
                        except (ValueError, SyntaxError) as e:
                            print(f"Errore nella valutazione della stringa input per {p_name}: {e}")
                            input_data = []
                    
                    if not isinstance(input_data, list):
                        input_data = []

                output_data = []
                if 'output' in item:
                    output_data = item['output']
                    if p_name in problematic_problems and isinstance(output_data, str):
                        try:
                            output_data = literal_eval(output_data)
                        except (ValueError, SyntaxError) as e:
                            print(f"Errore nella valutazione della stringa output per {p_name}: {e}")
                            output_data = []

                    if not isinstance(output_data, list):
                        output_data = []
                
                safe_len = min(len(input_data), len(output_data))
                
                for i in range(safe_len):
                    tests.append({"input": input_data[i], "output": output_data[i]})

    return tests

def _load_results(file_path):
    """
    Funzione ausiliaria per caricare i risultati da un file JSONL.
    """
    results = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Errore nel parsing della linea JSON: {e}")
    return results

def load_problem_data(p_name):
    """
    Carica tutti i dati relativi a un problema specifico, inclusi i risultati dinamici.
    """
    base_path = f"problems/human_eval/{p_name}"
    results_base_path = f"results/human_eval/{p_name}"
    data = {}
    
    with open(os.path.join(base_path, "problem.py"), "r") as f:
        data["PROBLEM_CODE"] = f.read()
    with open(os.path.join(base_path, "solution.py"), "r") as f:
        data["SOLUTION_CODE"] = f.read()
        
    data["FLOWCHART_PATHS"] = [f"data/human_eval/{p_name}/fc/l1.drawio.png", f"data/human_eval/{p_name}/fc/l2.drawio.png", f"data/human_eval/{p_name}/fc/l3.drawio.png"]
    data["BPMN_PATHS"] = [f"data/human_eval/{p_name}/bpmn/l1.drawio.png", f"data/human_eval/{p_name}/bpmn/l2.drawio.png", f"data/human_eval/{p_name}/bpmn/l3.drawio.png"]
    data["BLOCK_DIAGRAM_PATHS"] = [f"data/human_eval/{p_name}/block/l1.drawio.png"]
    
    data["OFFICIAL_TESTS"] = _load_test_cases(f"problems/human_eval/{p_name}/official.jsonl")
    data["GENERATED_TESTS"] = _load_test_cases(f"problems/human_eval/{p_name}/generated.jsonl")
    
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
                            match = re.search(r'^(l\d+)_(\w+)\.jsonl$', filename)
                            if match:
                                level, test_type = match.groups()
                                file_path = os.path.join(diagram_path, filename)
                                results = _load_results(file_path)
                                
                                if results:
                                    if level not in data["TEST_RESULTS"][model][diagram]:
                                        data["TEST_RESULTS"][model][diagram][level] = {}
                                    
                                    data["TEST_RESULTS"][model][diagram][level][test_type] = results

    return data
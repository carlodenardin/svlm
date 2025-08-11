import gradio as gr
import os
import re
import json
import ast
from PIL import Image
from tqdm import tqdm
from functools import partial
from src.core.model_manager import ModelManager
from src.core.code_executor import run_python_code
from src.core.gpu_utils import get_gpu_info_markdown
from src.data.problem_loader import load_problem_data, get_available_problems
from src.ui.components.problem_accordion import create_problem_accordion
from src.utils.const import MODEL_MAP

def load_image_from_selection(p_name, diagram_type, level):
    """
    Load an image based on problem, diagram type, and level.
    """
    if not all([p_name, diagram_type, level]):
        return None, "Please select a problem, diagram type, and level."

    diagram_map = {
        "Flowchart": "fc",
        "BPMN": "bpmn",
        "Block Diagram": "block"
    }

    diagram_folder = diagram_map.get(diagram_type)
    if not diagram_folder:
        return None, "Invalid diagram type selected."

    path = f"data/human_eval/{p_name}/{diagram_folder}/l{level}.drawio.png"
    if os.path.exists(path):
        return Image.open(path), f"Image loaded successfully from {os.path.basename(path)}"
    else:
        return None, f"Image not found at path: {path}"

def update_level_dropdown(diagram_type):
    """
    Update level dropdown based on diagram type.
    """
    if diagram_type == "Block Diagram":
        return gr.update(choices=["1"], value="1", interactive=False)
    else:
        return gr.update(choices=["1", "2", "3"], value="1", interactive=True)

def get_function_name(code):
    """
    Extract the first function name from the given Python code using AST.
    """
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
        return None
    except SyntaxError:
        return None

def run_bulk_test(model_manager, model_name, problems, diagrams, levels):
    """
    Execute bulk tests for selected problems, diagrams, and levels.
    """
    if model_manager.current_model is None:
        return "Nessun modello caricato. Caricare un modello prima di avviare il bulk test."
    
    total_tests = len(problems) * len(diagrams) * len(levels)
    completed_tests = 0
    results_summary = {}
    diagram_map = {"Flowchart": "fc", "BPMN": "bpmn", "Block Diagram": "block"}
    
    filtered_diagrams = {}
    for diag in diagrams:
        if diag == "Block Diagram":
            filtered_diagrams[diag] = [lvl for lvl in levels if lvl == "1"]
        else:
            filtered_diagrams[diag] = levels
    
    for p_name in tqdm(problems, desc="Problemi"):
        results_summary[p_name] = {}
        problem_data = load_problem_data(p_name)
        problem_prompt = problem_data["PROBLEM_CODE"]
        official_tests = problem_data["OFFICIAL_TESTS"]
        generated_tests = problem_data["GENERATED_TESTS"]
        
        for diagram_type_name, level_list in filtered_diagrams.items():
            results_summary[p_name][diagram_type_name] = {}
            diagram_folder = diagram_map.get(diagram_type_name)
            
            for level in level_list:
                completed_tests += 1
                yield f"Running test for Problem: {p_name}, Diagram: {diagram_type_name}, Level: {level} ({completed_tests}/{total_tests})"
                
                image_path = f"data/human_eval/{p_name}/{diagram_folder}/l{level}.drawio.png"
                if not os.path.exists(image_path):
                    error_message = f"Image not found at {image_path}"
                    results_summary[p_name][diagram_type_name][f"l{level}"] = error_message
                    yield error_message
                    continue

                try:
                    image_input = Image.open(image_path)
                    model_answer = model_manager.generate_response(image_input, problem_prompt)
                    
                    # Extract Python code
                    code_pattern = r"```python\n(.*?)\n```"
                    match = re.search(code_pattern, model_answer, re.DOTALL)
                    if match:
                        python_code = match.group(1).strip()
                    else:
                        python_code = model_answer.strip()
                        yield f"Warning: No ```python``` block found in model response for {p_name}-{diagram_type_name}-l{level}. Saving raw response."
                    
                    # Save the extracted Python code
                    output_dir = f"results/human_eval/{p_name}/{model_name}/{diagram_folder}"
                    os.makedirs(output_dir, exist_ok=True)
                    output_file_path = os.path.join(output_dir, f"l{level}.py")
                    
                    with open(output_file_path, 'w') as f:
                        f.write(python_code)
                    
                    # Extract function name
                    func_name = get_function_name(python_code)
                    if not func_name:
                        error_message = f"No valid function found in generated code for {p_name}-{diagram_type_name}-l{level}"
                        results_summary[p_name][diagram_type_name][f"l{level}"] = error_message
                        yield error_message
                        # Save empty test results
                        for test_type in ["official", "generated"]:
                            test_output_file = os.path.join(output_dir, f"l{level}_{test_type}.jsonl")
                            with open(test_output_file, 'w') as f:
                                for test in problem_data[f"{test_type.upper()}_TESTS"]:
                                    f.write(json.dumps({
                                        "success": False,
                                        "error": "No valid function defined in generated code",
                                        "input": test["input"],
                                        "output": "",
                                        "expected output": str(test["output"])
                                    }) + '\n')
                        continue
                    
                    # Run tests and save results
                    test_results = {
                        "official": [],
                        "generated": []
                    }
                    for test_type, tests in [("official", official_tests), ("generated", generated_tests)]:
                        for test in tests:
                            test_input = test["input"]
                            expected_output = test["output"]
                            try:
                                exec_code = f"{python_code}\nresult = {func_name}({repr(test_input)})"
                                local_vars = {}
                                exec(exec_code, {}, local_vars)
                                output = local_vars.get("result")
                                success = str(output) == str(expected_output)
                                error = ""
                            except Exception as e:
                                success = False
                                error = str(e)
                                output = None
                            
                            test_results[test_type].append({
                                "success": success,
                                "error": error,
                                "input": test_input,
                                "output": str(output) if output is not None else "",
                                "expected output": str(expected_output)
                            })
                        
                        # Save test results
                        test_output_file = os.path.join(output_dir, f"l{level}_{test_type}.jsonl")
                        with open(test_output_file, 'w') as f:
                            for result in test_results[test_type]:
                                f.write(json.dumps(result) + '\n')
                    
                    results_summary[p_name][diagram_type_name][f"l{level}"] = (
                        f"Generated code saved in {output_file_path}\n"
                        f"Official test results saved in {os.path.join(output_dir, f'l{level}_official.jsonl')}\n"
                        f"Generated test results saved in {os.path.join(output_dir, f'l{level}_generated.jsonl')}"
                    )
                    
                except Exception as e:
                    error_message = f"Errore durante l'esecuzione del test per {p_name}-{diagram_type_name}-l{level}: {e}"
                    results_summary[p_name][diagram_type_name][f"l{level}"] = error_message
                    yield error_message

    final_summary_text = "Bulk Test Completato. Riepilogo:\n"
    for p, d in results_summary.items():
        final_summary_text += f"\n- Problema: {p}\n"
        for d_name, l_res in d.items():
            final_summary_text += f"  - Diagramma: {d_name}\n"
            for l_name, l_msg in l_res.items():
                final_summary_text += f"    - {l_name}: {l_msg}\n"
    
    yield final_summary_text

def create_gradio_interface():
    """
    Create the main Gradio interface for the application.
    """
    with open("css/styles.css", "r") as f:
        custom_css = f.read()
    
    model_manager = ModelManager()
    available_problems = get_available_problems()
    
    with gr.Blocks(css=custom_css) as demo:
        with gr.Row():
            gr.Markdown("")
            gpu_info_markdown = gr.Markdown(get_gpu_info_markdown())
            timer = gr.Timer(3).tick(get_gpu_info_markdown, outputs=gpu_info_markdown)

        with gr.Tabs() as tabs:
            with gr.Tab("Home"):
                gr.Markdown("# Small Vision Language Model - Image Text to Code")
                gr.Markdown(
                    "This repository provides a benchmark for evaluating multimodal models in the task of code generation from graphical representations. The dataset was built by selecting problems from Human-Eval and PSB2, specifically."
                )
                
                with gr.Accordion("Human-Eval", open=False):
                    gr.Markdown("---")
                    for problem in available_problems:
                        create_problem_accordion(problem)
                
                with gr.Accordion("PSB2", open=False):
                    gr.Markdown("Questa sezione contiene le specifiche del modello e altre informazioni tecniche.")
            
            with gr.Tab("On-The-Fly Test"):
                gr.Markdown("# Model Selection")
                with gr.Row(variant="panel"):
                    with gr.Row():
                        model_selector = gr.Dropdown(
                            choices=list(MODEL_MAP.keys()),
                            label="Select a Model",
                            scale=2
                        )
                        with gr.Column(scale=1):
                            load_button = gr.Button("Load Model")
                            unload_button = gr.Button("Unload Model")
                        with gr.Column(scale=1):
                            status_output = gr.Textbox(label="Status", value="No model is currently loaded.")
                
                gr.Markdown("---")
                
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("## Model Inference")
                        
                        with gr.Accordion("Load Image from Dataset", open=False):
                            with gr.Row():
                                problem_dropdown = gr.Dropdown(
                                    choices=available_problems,
                                    label="Select Problem",
                                    value=available_problems[0] if available_problems else None
                                )
                                diagram_dropdown = gr.Dropdown(
                                    choices=["Flowchart", "BPMN", "Block Diagram"],
                                    label="Select Diagram Type"
                                )
                                level_dropdown = gr.Dropdown(
                                    choices=["1", "2", "3"],
                                    label="Select Level",
                                    value="1"
                                )
                            load_image_button = gr.Button("Load Image")
                            load_image_status = gr.Textbox(label="Image Status", interactive=False)
                        
                        image_input = gr.Image(type="pil", label="Image Input", interactive=True)
                        prompt_input = gr.Textbox(label="Enter your prompt here")
                        generate_button = gr.Button("Generate Response")
                        model_output = gr.Textbox(label="Model Response")
                    
                    with gr.Column(scale=1):
                        gr.Markdown("## Code Executor")
                        code_input = gr.Code(
                            language="python",
                            label="Python Code",
                        )
                        run_btn = gr.Button("Run Code")
                        code_output = gr.Textbox(label="Code Output")
                
                load_button.click(model_manager.load_model, inputs=model_selector, outputs=status_output)
                unload_button.click(model_manager.unload_model, inputs=None, outputs=status_output)
                generate_button.click(model_manager.generate_response, inputs=[image_input, prompt_input], outputs=[model_output])
                run_btn.click(run_python_code, inputs=code_input, outputs=code_output)

                diagram_dropdown.change(
                    fn=update_level_dropdown,
                    inputs=diagram_dropdown,
                    outputs=level_dropdown
                )

                load_image_button.click(
                    fn=load_image_from_selection,
                    inputs=[problem_dropdown, diagram_dropdown, level_dropdown],
                    outputs=[image_input, load_image_status]
                )

            with gr.Tab("Bulk Test"):
                gr.Markdown("# Bulk Test Execution")
                
                with gr.Row(variant="panel"):
                    with gr.Column(scale=1):
                        bulk_test_model_selector = gr.Dropdown(
                            choices=list(MODEL_MAP.keys()),
                            label="Select Model for Bulk Test",
                            scale=2
                        )
                        with gr.Row():
                            bulk_load_button = gr.Button("Load Model")
                            bulk_unload_button = gr.Button("Unload Model")
                        bulk_status_output = gr.Textbox(label="Model Status", value="No model loaded for bulk tests.")
                
                gr.Markdown("---")
                
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("## Test Settings")
                        selected_problems = gr.CheckboxGroup(choices=available_problems, label="Select Problems to Test")
                        selected_diagrams = gr.CheckboxGroup(choices=["Flowchart", "BPMN", "Block Diagram"], label="Select Diagram Types")
                        selected_levels = gr.CheckboxGroup(choices=["1", "2", "3"], label="Select Levels")
                        
                        start_bulk_test_button = gr.Button("Start Bulk Test", variant="primary")
                        
                gr.Markdown("---")
                bulk_output = gr.Textbox(label="Bulk Test Output", lines=20)
                
                bulk_load_button.click(model_manager.load_model, inputs=bulk_test_model_selector, outputs=bulk_status_output)
                bulk_unload_button.click(model_manager.unload_model, inputs=None, outputs=bulk_status_output)
                start_bulk_test_button.click(
                    fn=partial(run_bulk_test, model_manager),
                    inputs=[bulk_test_model_selector, selected_problems, selected_diagrams, selected_levels],
                    outputs=bulk_output
                )

    return demo
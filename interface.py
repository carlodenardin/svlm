import torch
from transformers import AutoModel, AutoTokenizer
import gradio as gr
import io
import contextlib
import pynvml as nvml
import os
from PIL import Image
from tqdm import tqdm
import json

# Importa i moduli necessari dal tuo progetto
from src.utils.const import MODEL_MAP
from src.utils.utils import create_problem_accordion, load_problem_data, _load_test_cases

# Variabili globali per lo stato del modello
current_model, current_tokenizer, current_model_name = None, None, None

def load_model(model_name: str):
    global current_model, current_tokenizer, current_model_name
    if model_name == current_model_name:
        return f"Model {model_name} is already loaded", gr.update(visible=True)
    unload_model()
    try:
        model_id = MODEL_MAP[model_name]
        current_model = AutoModel.from_pretrained(
            model_id, trust_remote_code=True, attn_implementation='sdpa', torch_dtype=torch.bfloat16
        ).eval().cuda()
        current_tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
        current_model_name = model_name
        return f"Model '{model_name}' loaded successfully", gr.update(visible=True)
    except Exception as e:
        current_model_name = None
        return f"Failed to load model '{model_name}': {e}", gr.update(visible=False)

def unload_model():
    global current_model, current_tokenizer, current_model_name
    if current_model is not None:
        del current_model
        del current_tokenizer
        torch.cuda.empty_cache()
        current_model, current_tokenizer, current_model_name = None, None, None
        return "No model is currently loaded.", gr.update(visible=False)
    return "No model is currently loaded.", gr.update(visible=False)

def generate_response(image_input, prompt_input):
    if current_model is None:
        return "Load a model first."
    if image_input is None or not prompt_input.strip():
        return "Please provide both an image and a prompt."
    msgs = [{'role': 'user', 'content': [image_input, prompt_input]}]
    answer = current_model.chat(
        msgs=msgs,
        image=image_input,
        tokenizer=current_tokenizer
    )
    return answer

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

def get_gpu_info_markdown():
    try:
        nvml.nvmlInit()
        handle = nvml.nvmlDeviceGetHandleByIndex(0)
        name = nvml.nvmlDeviceGetName(handle)
        info = nvml.nvmlDeviceGetMemoryInfo(handle)
        total_mem_mib = info.total // (1024 * 1024)
        used_mem_mib = info.used // (1024 * 1024)
        
        return (
            f"### GPU Stats\n"
            f"```\n"
            f"Name: {name}\n"
            f"Memory: {used_mem_mib} MiB / {total_mem_mib} MiB\n"
            f"```"
        )
    except Exception:
        return "### GPU Stats\n```\nGPU information not available.\n```"

def load_image_from_selection(p_name, diagram_type, level):
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
    if diagram_type == "Block Diagram":
        return gr.update(choices=["1"], value="1", interactive=False)
    else:
        return gr.update(choices=["1", "2", "3"], value="1", interactive=True)

def get_available_problems():
    problems_path = "problems/human_eval"
    if not os.path.exists(problems_path):
        return []

    problems = [d for d in os.listdir(problems_path) if os.path.isdir(os.path.join(problems_path, d))]
    problems.sort()
    return problems

def run_bulk_test(model_name, problems, diagrams, levels):
    if current_model is None:
        return "Nessun modello caricato. Caricare un modello prima di avviare il bulk test."
    
    total_tests = len(problems) * len(diagrams) * len(levels)
    completed_tests = 0
    results_summary = {}
    
    # Mappa i nomi completi dei diagrammi alle loro abbreviazioni
    diagram_map = {"Flowchart": "fc", "BPMN": "bpmn", "Block Diagram": "block"}
    
    # Filtra i livelli in base al diagramma
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
        
        for diagram_type_name, level_list in filtered_diagrams.items():
            results_summary[p_name][diagram_type_name] = {}
            diagram_folder = diagram_map.get(diagram_type_name)
            
            for level in level_list:
                completed_tests += 1
                yield f"Running test for Problem: {p_name}, Diagram: {diagram_type_name}, Level: {level} ({completed_tests}/{total_tests})"
                
                image_path = f"data/human_eval/{p_name}/{diagram_folder}/l{level}.drawio.png"
                if not os.path.exists(image_path):
                    continue

                try:
                    image_input = Image.open(image_path)
                    
                    # Genera la risposta del modello
                    msgs = [{'role': 'user', 'content': [image_input, problem_prompt]}]
                    model_answer = current_model.chat(msgs=msgs, image=image_input, tokenizer=current_tokenizer)
                    
                    # --- MOCKUP della valutazione ---
                    # Invece di eseguire la valutazione, creiamo un risultato fittizio
                    mock_results = [
                        {"task_id": f"{p_name}-{diagram_folder}-l{level}", "completion": model_answer, "success": True, "details": "Mockup result - SUCCESS"},
                        {"task_id": f"{p_name}-{diagram_folder}-l{level}", "completion": model_answer, "success": False, "details": "Mockup result - FAILURE"}
                    ]

                    # Salva i risultati in un file JSONL
                    output_dir = f"results/human_eval/{p_name}/{model_name}/{diagram_folder}"
                    os.makedirs(output_dir, exist_ok=True)
                    output_file_path = os.path.join(output_dir, f"l{level}_generated.jsonl")
                    
                    with open(output_file_path, 'w') as f:
                        for result in mock_results:
                            f.write(json.dumps(result) + '\n')
                    
                    results_summary[p_name][diagram_type_name][f"l{level}"] = f"Test completato. Risultati mockup salvati in {output_file_path}"
                    
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

# --- CSS per migliorare la UI/UX ---
custom_css = """
/* ... (codice CSS invariato) ... */
body {
    background-color: #121212;
    color: #E0E0E0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1 {
    color: #4CAF50;
    border-bottom: 2px solid #4CAF50;
    padding-bottom: 5px;
}
h2 {
    color: #FFC107;
    border-bottom: 1px dashed #FFC107;
    padding-bottom: 3px;
}
h3 {
    color: #03A9F4;
}
.gradio-tabs .gradio-tab.selected {
    border-bottom: 3px solid #4CAF50 !important;
}
.gradio-tabs .gradio-tab {
    color: #E0E0E0 !important;
    background-color: #2c2c2c !important;
    border-color: #3e3e3e !important;
}
.gradio-accordion .label-wrap {
    background-color: #2c2c2c !important;
    border: 1px solid #3e3e3e !important;
    border-radius: 5px;
    margin-top: 10px;
}
.gradio-accordion .label-wrap .label {
    color: #E0E0E0 !important;
    font-size: 1.1em;
    font-weight: bold;
}
.gradio-accordion.open > .label-wrap {
    background-color: #3e3e3e !important;
}
.gradio-input, .gradio-dropdown, .gradio-code {
    background-color: #1e1e1e !important;
    border: 1px solid #555 !important;
    color: #E0E0E0 !important;
}
.gradio-output {
    background-color: #1e1e1e !important;
    border: 1px solid #555 !important;
    color: #E0E0E0 !important;
}
.gradio-button {
    background-color: #555 !important;
    color: #E0E0E0 !important;
    border: none !important;
}
.gradio-button:hover {
    background-color: #666 !important;
}
.gradio-button[label="Load Model"] {
    background-color: #4CAF50 !important;
    color: #FFFFFF !important;
}
.gradio-button[label="Unload Model"] {
    background-color: #f44336 !important; /* Rosso */
    color: #FFFFFF !important;
}
.gradio-button[label="Generate Response"], .gradio-button[label="Run Code"], .gradio-button[label="Load Image"] {
    background-color: #03A9F4 !important; /* Blu */
    color: #FFFFFF !important;
}
"""

# Prende la lista dei problemi all'avvio
available_problems = get_available_problems()

with gr.Blocks(css=custom_css) as demo:
    with gr.Row():
        gr.Markdown("")
        gpu_info_markdown = gr.Markdown(get_gpu_info_markdown())
        timer = gr.Timer(3).tick(get_gpu_info_markdown, outputs=gpu_info_markdown)

    with gr.Tabs() as tabs:
        with gr.Tab("Home"):
            gr.Markdown("# Small Vision Languange Model - Image Text to Code")
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
            
            load_button.click(load_model, inputs=model_selector, outputs=status_output)
            unload_button.click(unload_model, inputs=None, outputs=status_output)
            generate_button.click(generate_response, inputs=[image_input, prompt_input], outputs=[model_output])
            run_btn.click(fn=run_python_code, inputs=code_input, outputs=code_output)

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
            
            bulk_load_button.click(load_model, inputs=bulk_test_model_selector, outputs=bulk_status_output)
            bulk_unload_button.click(unload_model, inputs=None, outputs=bulk_status_output)
            start_bulk_test_button.click(
                fn=run_bulk_test,
                inputs=[bulk_test_model_selector, selected_problems, selected_diagrams, selected_levels],
                outputs=bulk_output
            )

demo.launch(share=False)
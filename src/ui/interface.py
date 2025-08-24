from functools import partial
from PIL import Image
from src.core.model_manager import ModelManager
from src.core.run_tests import run_bulk_response_test, run_reasoning_response_test
from src.core.run_tests_code import run_bulk_code_test
from src.utils.const import MODEL_MAP, DIAGRAMS_LEVELS, DIAGRAMS_TYPES, DIAGRAM_MAP, PROMPT
from src.utils.utils import get_css_style, get_gpu_info, update_link, get_available_problems

import gradio as gr
import os

def load_image_from_selection(problem, type, level):

    diagram_folder = DIAGRAM_MAP.get(type)

    if os.path.exists(f"data/human_eval/{problem}/{diagram_folder}/l{level}.drawio.png"):
        return Image.open(f"data/human_eval/{problem}/{diagram_folder}/l{level}.drawio.png")
    else:
        return None

def update_level_dropdown(type):
    if type == "Block Diagram":
        return gr.update(choices = ["1"], value = "1", interactive = False)
    else:
        return gr.update(choices = DIAGRAMS_LEVELS, value = "1", interactive = True)

def create_gradio_interface():
    """
        Application Interface composed by 2 tab:
        - On The Fly: can be used to perform quick test with the available models
        - Bulk Test: can be used to perform bulk test
    """

    model_manager = ModelManager()
    available_problems = get_available_problems()
    
    with gr.Blocks(css = get_css_style()) as demo:

        with gr.Row():
            with gr.Column(scale = 3):
                gr.Markdown("# Model Selection")
                with gr.Row(variant = "panel"):
                    with gr.Row():
                        with gr.Column():
                            with gr.Row():
                                model_selector = gr.Dropdown(
                                    choices = list(MODEL_MAP.keys()),
                                    label = "Select a Model",
                                    scale = 2,
                                    value = None
                                )
                        with gr.Column():   
                            with gr.Row():
                                with gr.Column():   
                                    load_button = gr.Button("Load Model", variant = "primary")
                                    unload_button = gr.Button("Unload Model")
                                status_output = gr.Textbox(label = "Status", value = "", interactive = False)
            with gr.Column():
                gr.Markdown("# GPU Stats")
                gpu_info_markdown = gr.Markdown(get_gpu_info())
                timer = gr.Timer(3).tick(get_gpu_info, outputs = gpu_info_markdown)
                hf_link = gr.Markdown(value = "")

        gr.Markdown("<br><br>")
                
        gr.Markdown("## Model Inference")
        with gr.Row():
            with gr.Column(scale=1):
                
                with gr.Accordion("Load Image from Dataset", open = False):
                    with gr.Row():
                        problem_dropdown = gr.Dropdown(
                            choices = available_problems,
                            label = "Select Problem",
                        )
                        diagram_dropdown = gr.Dropdown(
                            choices = DIAGRAMS_TYPES,
                            label = "Select Diagram Type"
                        )
                        level_dropdown = gr.Dropdown(
                            choices = DIAGRAMS_LEVELS,
                            label = "Select Level",
                        )
                    load_image_button = gr.Button("Load Image")
                
                image_input = gr.Image(type = "pil", label = "Image Input", interactive = True)
                
            
            with gr.Column(scale = 1):
                prompt_input = gr.Textbox(label = "Prompt")
                generate_button = gr.Button("Generate Response")
                model_output = gr.Textbox(label = "Response")


        generate_button.click(model_manager.generate_response, inputs = [image_input, prompt_input], outputs = [model_output])

        diagram_dropdown.change(
            fn = update_level_dropdown,
            inputs = diagram_dropdown,
            outputs = level_dropdown
        )

        load_image_button.click(
            fn = load_image_from_selection,
            inputs = [problem_dropdown, diagram_dropdown, level_dropdown],
            outputs = [image_input]
        )   
            
        load_button.click(model_manager.load_model, inputs = model_selector, outputs = status_output)
        unload_button.click(model_manager.unload_model, outputs = status_output)
        model_selector.change(update_link, inputs=model_selector, outputs = hf_link)

    return demo
import os
import re
import json
import ast
import torch
import gc
import timeout_decorator
import sys
import gradio as gr
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PIL import Image
from tqdm import tqdm
from src.utils.const import DIAGRAM_MAP, PATTERN, MODEL_MAP, PROMPT, PROMPT2
from src.core.model_manager import ModelManager
    
def _generate_response(model_manager, image, prompt):
    """
    Generate a response using the loaded model
    """
    try:
        return model_manager.generate_response(image, prompt)
    except Exception as e:
        print(f"Error generating response: {e}")
        return ""
    
def run_bulk_response_test(model_manager, problems, diagrams, levels, prompt, progress = gr.Progress()):
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
    7a. Generate a second response (explanation of the problem)
    7b. Save the response
    """
    
    total_tests = len(problems) * len(diagrams) * len(levels)
    count = 0
    
    filtered_diagrams = {}
    for diag in diagrams:
        if diag == "Block Diagram":
            filtered_diagrams[diag] = [lvl for lvl in levels if lvl == "1"]
        else:
            filtered_diagrams[diag] = levels

    for problem in problems:
        for diagram, level_list in filtered_diagrams.items():
            diagram_folder = DIAGRAM_MAP.get(diagram)
            
            for level in level_list:
                progress(count / total_tests, desc=f"Testing: {problem} / {diagram} / L{level}")

                count += 1
                
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
                    yield "Error: Model response was empty"
                    continue

                response_dir = os.path.join("results/human_eval", problem, model_manager.model_name, diagram_folder)
                os.makedirs(response_dir, exist_ok=True)
                
                response_path = os.path.join(response_dir, f"l{level}_response.txt")
                with open(response_path, "w") as f:
                    f.write(response)

                try:
                    image = Image.open(image_path)
                except FileNotFoundError:
                    yield f"Error: Image not found at {image_path}"
                    continue
                
                try:
                    response = _generate_response(model_manager, image, PROMPT2)
                finally:
                    image.close()

                if not response:
                    yield "Error: Model response was empty."
                    continue

                response_dir = os.path.join("results/human_eval", problem, model_manager.model_name, diagram_folder)
                os.makedirs(response_dir, exist_ok=True)
                
                response_path = os.path.join(response_dir, f"l{level}_response_understanding.txt")
                with open(response_path, "w") as f:
                    f.write(response)
                
                torch.cuda.empty_cache()

    yield "Bulk test completed."
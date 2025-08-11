import gradio as gr
import pandas as pd
import os

def create_results_table_block(results, test_type):
    """
    Create a table block for test results.
    """
    if not results:
        return gr.Markdown(f"No {test_type} results available.")
    
    df = pd.DataFrame(results)
    if df.empty:
        return gr.Markdown(f"No {test_type} results available.")
    
    with gr.Group():
        gr.Markdown(f"### {test_type} Test Results")
        return gr.DataFrame(df, label=f"{test_type} Results")

def create_problem_accordion(p_name):
    """
    Create an accordion for a specific problem, including code, images, and results.
    """
    from src.data.problem_loader import load_problem_data
    
    data = load_problem_data(p_name)
    
    with gr.Accordion(f"Problem {p_name}", open=False):
        with gr.Tabs():
            with gr.Tab("Problem"):
                gr.Code(data["PROBLEM_CODE"], language="python", label="Problem Code")
            
            with gr.Tab("Solution"):
                gr.Code(data["SOLUTION_CODE"], language="python", label="Solution Code")
            
            with gr.Tab("Diagrams"):
                with gr.Tabs():
                    with gr.Tab("Flowchart"):
                        with gr.Row():
                            for path in data["FLOWCHART_PATHS"]:
                                level = path.split('/')[-1].split('.')[0]
                                if os.path.exists(path):
                                    gr.Image(path, label=f"Flowchart {level}", width=300)
                                else:
                                    gr.Markdown(f"No image available for Flowchart {level}")
                    with gr.Tab("BPMN"):
                        with gr.Row():
                            for path in data["BPMN_PATHS"]:
                                level = path.split('/')[-1].split('.')[0]
                                if os.path.exists(path):
                                    gr.Image(path, label=f"BPMN {level}", width=300)
                                else:
                                    gr.Markdown(f"No image available for BPMN {level}")
                    with gr.Tab("Block Diagram"):
                        with gr.Row():
                            for path in data["BLOCK_DIAGRAM_PATHS"]:
                                level = path.split('/')[-1].split('.')[0]
                                if os.path.exists(path):
                                    gr.Image(path, label=f"Block Diagram {level}", width=300)
                                else:
                                    gr.Markdown(f"No image available for Block Diagram {level}")
            
            with gr.Tab("Results"):
                if not data["TEST_RESULTS"]:
                    gr.Markdown("No test results available.")
                else:
                    for model, diagrams in data["TEST_RESULTS"].items():
                        with gr.Accordion(model.upper(), open=False):
                            for diagram, levels in diagrams.items():
                                with gr.Accordion(diagram.upper(), open=False):
                                    sorted_levels = sorted(levels.keys())
                                    for level in sorted_levels:
                                        results = levels[level]
                                        with gr.Accordion(level.upper(), open=False):
                                            # Display generated code
                                            gr.Markdown(f"### Generated Code ({model}, {diagram}, {level})")
                                            if "code" in results and results["code"]:
                                                gr.Code(
                                                    results["code"],
                                                    language="python",
                                                    label=f"Generated Code for {model} ({diagram}, {level})",
                                                    lines=10,
                                                    show_label=True
                                                )
                                            else:
                                                gr.Markdown("No generated code available.")
                                            # Display test results
                                            if "official" in results:
                                                create_results_table_block(results["official"], "Official")
                                            if "generated" in results:
                                                create_results_table_block(results["generated"], "Generated")
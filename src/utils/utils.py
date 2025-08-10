import gradio as gr
import os
import json
import pandas as pd
from ast import literal_eval
import re # Importa il modulo per le espressioni regolari

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

def _update_test_output(input_val, tests):
    """
    Callback generica per aggiornare l'output di un test.
    """
    if input_val == "Select Input":
        return gr.update(value=""), gr.update(choices=["Select Input"] + [str(test['input']) for test in tests])

    for test_case in tests:
        if str(test_case['input']) == input_val:
            output = str(test_case['output'])
            new_choices = [str(test['input']) for test in tests]
            return gr.update(value=output), gr.update(choices=new_choices)
    
    return gr.update(value="Output non trovato."), gr.update()

def _create_interactive_test_block(tests, label):
    """
    Funzione ausiliaria che crea un blocco Gradio per i test interattivi.
    """
    test_inputs = [str(test['input']) for test in tests]
    dropdown_choices = ["Select Input"] + test_inputs

    with gr.Row():
        test_input_dropdown = gr.Dropdown(
            choices=dropdown_choices,
            label=label,
            value="Select Input",
            interactive=True
        )
        test_output_box = gr.Textbox(label="Output")
    
    tests_state = gr.State(value=tests)
    
    test_input_dropdown.change(
        fn=_update_test_output,
        inputs=[test_input_dropdown, tests_state],
        outputs=[test_output_box, test_input_dropdown]
    )

def _create_results_table_block(results, label):
    """
    Funzione ausiliaria per creare un blocco con la tabella dei risultati.
    """
    if not results:
        gr.Markdown(f"Nessun risultato disponibile per i test **{label}**.")
        return

    df = pd.DataFrame(results)
    
    # Calcola il numero di test passati, falliti e la percentuale
    num_tests = len(df)
    num_passed = df['success'].sum()
    num_failed = num_tests - num_passed
    success_rate = f"{(num_passed / num_tests) * 100:.0f}%" if num_tests > 0 else "0%"

    summary_text = f"{label} Test ({num_passed}/{num_tests} -> {success_rate})"
    
    def style_row_by_success(row):
        color = 'green' if row['success'] else 'red'
        return [f'color: {color};'] * len(row)

    styled_df = df.style.apply(style_row_by_success, axis=1)

    gr.Markdown(f"### {summary_text}")
    gr.Dataframe(
        value=styled_df,
        interactive=False,
    )

def create_problem_accordion(p_name):
    """
    Genera un blocco Accordion per un problema specifico.
    """
    data = load_problem_data(p_name)
    
    with gr.Accordion(p_name, open=False):
        with gr.Accordion("Definition", open=False):
            with gr.Accordion("Problem", open=False):
                gr.Code(
                    language="python",
                    value=data["PROBLEM_CODE"],
                    interactive=False
                )
            with gr.Accordion("Solution", open=False):
                gr.Code(
                    language="python",
                    value=data["SOLUTION_CODE"],
                    interactive=False
                )
            with gr.Accordion("Unit Test (Official)", open=False):
                _create_interactive_test_block(data["OFFICIAL_TESTS"], "Select Official Input")

            with gr.Accordion("Unit Test (Generated)", open=False):
                _create_interactive_test_block(data["GENERATED_TESTS"], "Select Generated Input")

        with gr.Accordion("Dataset", open=False):
            with gr.Accordion("Flowchart", open=False):
                with gr.Row():
                    for i, path in enumerate(data["FLOWCHART_PATHS"]):
                        if os.path.exists(path):
                            gr.Image(label=f"L{i+1}", value=path, show_label=True)
                        else:
                            gr.Markdown(f"Immagine L{i+1} non trovata.")
            with gr.Accordion("BPMN", open=False):
                with gr.Row():
                    for i, path in enumerate(data["BPMN_PATHS"]):
                        if os.path.exists(path):
                            gr.Image(label=f"L{i+1}", value=path, show_label=True)
                        else:
                            gr.Markdown(f"Immagine L{i+1} non trovata.")
            with gr.Accordion("Block Diagram", open=False):
                with gr.Row():
                    for i, path in enumerate(data["BLOCK_DIAGRAM_PATHS"]):
                        if os.path.exists(path):
                            gr.Image(label=f"L{i+1}", value=path, show_label=True)
                        else:
                            gr.Markdown(f"Immagine L{i+1} non trovata.")
        
        with gr.Accordion("Results", open=False):
            for model, diagrams in data["TEST_RESULTS"].items():
                with gr.Accordion(model.upper(), open=False):
                    for diagram, levels in diagrams.items():
                        with gr.Accordion(diagram.upper(), open=False):
                            sorted_levels = sorted(levels.keys())
                            for level in sorted_levels:
                                results = levels[level]
                                with gr.Accordion(level.upper(), open=False):
                                    if "official" in results:
                                        _create_results_table_block(results["official"], "Official")
                                    if "generated" in results:
                                        _create_results_table_block(results["generated"], "Generated")
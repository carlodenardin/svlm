import os
import re

def rename_results_files(base_path):
    """
    Rinomina i file dei risultati per i problemi di Human-Eval.

    Questa funzione scorre tutte le cartelle dei risultati dei problemi,
    cercando i file che terminano con "_generated.jsonl" o "_official.jsonl"
    e li rinomina per includere il livello (es. "l1_generated.jsonl").

    Args:
        base_path (str): Il percorso radice dove si trovano i risultati dei problemi.
                         Ad esempio: "results/human_eval"
    """
    
    # Scorri tutte le cartelle dei problemi (es. p120)
    for p_name in os.listdir(base_path):
        problem_path = os.path.join(base_path, p_name)
        if not os.path.isdir(problem_path):
            continue

        # Scorri le cartelle dei modelli (es. chatgpt)
        for model_name in os.listdir(problem_path):
            model_path = os.path.join(problem_path, model_name)
            if not os.path.isdir(model_path):
                continue

            # Scorri le cartelle dei diagrammi (es. fc, bpmn, block)
            for diagram_name in os.listdir(model_path):
                diagram_path = os.path.join(model_path, diagram_name)
                if not os.path.isdir(diagram_path):
                    continue

                # Cerca i file da rinominare
                for filename in os.listdir(diagram_path):
                    file_path = os.path.join(diagram_path, filename)
                    
                    # Usa le espressioni regolari per trovare il livello nel nome del file
                    match = re.search(r'l(\d+)', filename)
                    if match:
                        level = match.group(0) # es. "l1"
                        
                        # Controlla se il file contiene "generated" o "official"
                        if "generated" in filename and not filename.startswith(f"{level}_generated"):
                            new_filename = f"{level}_generated.jsonl"
                            os.rename(file_path, os.path.join(diagram_path, new_filename))
                            print(f"Rinominato {filename} -> {new_filename}")
                        elif "official" in filename and not filename.startswith(f"{level}_official"):
                            new_filename = f"{level}_official.jsonl"
                            os.rename(file_path, os.path.join(diagram_path, new_filename))
                            print(f"Rinominato {filename} -> {new_filename}")


rename_results_files("svlm/results/human_eval")
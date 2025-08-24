from ast import literal_eval
from src.utils.const import MODEL_MAP

import pynvml as nvml
import os
import pandas as pd
import json
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

def update_link(model_name):
    if model_name and model_name in MODEL_MAP:
        model_id = MODEL_MAP[model_name]["model"]
        return f'<a href="https://huggingface.co/{model_id}" target="_blank" style="text-decoration: none;">https://huggingface.co/{model_id}</a>'
    return ""

def get_available_problems():
    problems_path = "problems/human_eval"
    if not os.path.exists(problems_path):
        return []
    problems = [d for d in os.listdir(problems_path) if os.path.isdir(os.path.join(problems_path, d))]
    problems.sort()
    return problems

def sanitize_sheet_name(name):
    """
    Pulisce e accorcia un nome per renderlo valido come nome di un foglio Excel.
    (Max 31 caratteri, no caratteri proibiti).
    """
    invalid_chars = r'[\\/*?:"<>|]'
    name = re.sub(invalid_chars, '_', name)
    return name[:31]

def creare_report_excel(cartella_base):
    """
    Scansiona una struttura di cartelle complessa (problema/modello/diagramma),
    raccoglie i dati e crea un file Excel con un foglio per ogni modello.

    Args:
        cartella_base (str): Il percorso della cartella principale (es. 'results/human_eval').
        nome_file_output (str): Il nome del file Excel da creare (es. 'report_completo.xlsx').
    """
    # NUOVO: Usiamo un dizionario per separare i dati per ogni modello
    dati_per_modello = {}
    
    if not os.path.isdir(cartella_base):
        print(f"Errore: La cartella '{cartella_base}' non è stata trovata.")
        return

    print(f"🔍 Inizio la scansione della cartella '{cartella_base}'...")

    for root, dirs, files in os.walk(cartella_base):
        for nome_file in files:
            if nome_file.endswith('.jsonl') and "reasoning":
                percorso_completo = os.path.join(root, nome_file)
                
                try:
                    # --- NUOVA Logica di Estrazione delle Informazioni ---
                    
                    # Calcoliamo il percorso relativo dalla cartella base per estrarre le parti
                    percorso_relativo = os.path.relpath(root, cartella_base)
                    parti_percorso = percorso_relativo.split(os.sep)
                    
                    # La struttura attesa è: problema/modello/diagramma
                    if len(parti_percorso) < 3:
                        # Se il percorso non è abbastanza "profondo", lo saltiamo
                        continue
                        
                    nome_problema = parti_percorso[0]
                    nome_modello = parti_percorso[1]
                    nome_diagramma = parti_percorso[2]
                    
                    match = re.search(r'l(\d+)_', nome_file)
                    if not match:
                        continue
                    livello = match.group(1)

                    # --- Lettura del file .jsonl (invariata) ---
                    with open(percorso_completo, 'r', encoding='utf-8') as f:
                        for linea in f:
                            riga_dati = json.loads(linea)
                            
                            # NUOVO: Aggiunta la colonna 'problem'
                            riga_report = {
                                'problem': nome_problema,
                                'diagram': nome_diagramma,
                                'level': livello,
                                'success': 0 if not riga_dati.get('success') else 1,
                                'input': str(riga_dati.get('input')),
                                'output': riga_dati.get('output'),
                                'correct output': riga_dati.get('correct_output'),
                                'error': riga_dati.get('error')
                            }
                            
                            # NUOVO: Aggiungiamo la riga alla lista corretta nel dizionario
                            if nome_modello not in dati_per_modello:
                                dati_per_modello[nome_modello] = []
                            dati_per_modello[nome_modello].append(riga_report)
                
                except Exception as e:
                    print(f"⚠️ Si è verificato un errore durante l'elaborazione del file {percorso_completo}: {e}")

    if not dati_per_modello:
        print("❌ Nessun dato trovato. Il file Excel non sarà creato.")
        return

    # --- NUOVA Logica di Creazione del file Excel Multi-Foglio ---
    print(f"\n📊 Trovati dati per {len(dati_per_modello)} modelli. Creo il file Excel multi-foglio...")
    
    # Usiamo ExcelWriter per poter scrivere su più fogli nello stesso file
    with pd.ExcelWriter("results.xlsx", engine='openpyxl') as writer:
        for nome_modello, dati in dati_per_modello.items():
            print(f"  -> Elaboro il foglio per il modello: '{nome_modello}' ({len(dati)} righe)")
            
            df_modello = pd.DataFrame(dati)
            
            # Pulisce il nome del modello per renderlo un nome di foglio valido
            nome_foglio_sicuro = sanitize_sheet_name(nome_modello)
            
            # Scrive il DataFrame del modello specifico nel suo foglio
            df_modello.to_excel(writer, sheet_name=nome_foglio_sicuro, index=False)
    
    print(f"✅ Fatto! Il file Excel results.xlsx è stato creato con successo.")


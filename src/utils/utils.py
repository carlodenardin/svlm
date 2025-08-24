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

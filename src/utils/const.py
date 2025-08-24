from src.core.models.llava_model import LlavaModel
from src.core.models.minicpmv4_model import MiniCPMV4Model
from src.core.models.gemma_model import GemmaModel
from src.core.models.gemma_quant_model import GemmaQuantModel
from src.core.models.perception_model import PerceptionModel
from src.core.models.lfm2_vl_model import LFM2
from src.core.models.lfm2_vl_1B_model import LFM21B
from src.core.models.paligemma2_model import PaliGemma2Model
from src.core.models.gpt5_nano import GPT5NanoModel

MODEL_MAP = {
    "Gemma 3 4B": {
        "name": "Gemma 3 4B",
        "model": "google/gemma-3-4b-it",
        "class": GemmaModel
    },
    "Gemma 3 4B 4bit": {
        "name": "Gemma 3 4B 4bit",
        "model": "unsloth/gemma-3-4b-it-bnb-4bit",
        "class": GemmaQuantModel
    },
    "GPT5 Nano": {
        "name": "GPT5 Nano",
        "model": "gpt-5-nano",
        "class": GPT5NanoModel
    },
    "LFM2 VL 450M": {
        "name": "LFM2 VL 450M",
        "model": "LiquidAI/LFM2-VL-450M",
        "class": LFM2
    },
    "LFM2 VL 1.6B": {
        "name": "LFM2 VL 1.6B",
        "model": "LiquidAI/LFM2-VL-1.6B",
        "class": LFM21B
    },
    "LLaVA 1.5 7B 4bit": {
        "name": "LLaVA 1.5 7B 4bit",
        "model": "unsloth/llava-1.5-7b-hf-bnb-4bit",
        "class": LlavaModel
    },
    "MiniCPM V 4.0": {
        "name": "MiniCPM V 4.0",
        "model": "openbmb/MiniCPM-V-4",
        "class": MiniCPMV4Model
    },
    "Paligemma2 3B Mix": {
        "name": "Paligemma2 3B Mix",
        "model": "google/paligemma2-3b-mix-448",
        "class": PaliGemma2Model
    },
    "Perception LM 1B 8bit": {
        "name": "Perception LM 1B 8bit",
        "model": "facebook/Perception-LM-1B",
        "class": PerceptionModel
    },
}

DIAGRAMS_TYPES = ['Flowchart', 'BPMN', 'Block Diagram']

DIAGRAMS_LEVELS = ["1", "2", "3"]

DIAGRAM_MAP = {
    "Flowchart": "fc",
    "BPMN": "bpmn",
    "Block Diagram": "block"
}

PROMPT = """You are a Python code generation assistant. Given a diagram of an algorithm, generate a single, syntactically correct function that implements the logic shown. Return only the Python code, enclosed in a ```python``` block."""

PROMPT2 = """You are a software engineer. Given an image of a flowchart, describe the algorithm's implementation using a step-by-step process. Your response should include:
- A brief overview of the algorithm's purpose.
- The input data required.
- The main logical flow, detailing decisions, loops, and function calls.
- The expected output.
Present the information clearly and concisely, ready for implementation."""

PROMPT3 = """Below you are given the reasoning of a small VLM about how to solve a problem. Your task is to strictly follow this reasoning and translate it into executable Python function, without improving or changing the approach. Output only the code inside python ```python ```"""

PATTERN = r"```python\n(.*?)\n```"
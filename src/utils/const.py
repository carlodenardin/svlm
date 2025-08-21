from src.core.models.deepseekvl2small_model import DeepSeekVlModel
from src.core.models.llava_model import LlavaModel
from src.core.models.minicpmv4_model import MiniCPMV4Model
from src.core.models.gemma_model import GemmaModel
from src.core.models.gemma_quant_model import GemmaQuantModel
from src.core.models.perception_model import PerceptionModel
from src.core.models.lfm2_vl_model import LFM2
from src.core.models.lfm2_vl_1B_model import LFM21B

MODEL_MAP = {
    #"DeepSeek VL2 Tiny": {
    #    "name": "DeepSeek VL2 Tiny",
    #    "model": "deepseek-ai/deepseek-vl2-tiny",
    #    "class": DeepSeekVlModel
    #},
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

PATTERN = r"```python\n(.*?)\n```"
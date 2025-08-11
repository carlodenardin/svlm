MODEL_MAP = {
    "MiniCPM-V-4": {
        "name": "MiniCPM-V-4",
        "model": "openbmb/MiniCPM-V-4",
        "max_tokens": 512
    },
    "llava": {
        "name": "LLaVA",
        "model": "llava-hf/llava-1.5-7b-hf",
        "max_tokens": 512,
        "quantization": "4bit",  # Use 4-bit quantization for memory efficiency
        "torch_dtype": "float16"  # Use float16 for GPU efficiency
    }
}
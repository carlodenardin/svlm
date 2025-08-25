# Small Vision Language Model - Image Text to Code

This project provides a benchmark for evaluating multimodal models in the task of code generation from graphical representations using problems from HumanEval.

## Project Structure
```
project/
├── data/human_eval				# Data folder
│   ├── p084/               	# Specific single problem
│	│   ├── block/
│	│	│   ├── l1.drawio  		# Block diagram level 1 drawio
│	│	│   ├── l1.drawio.png  	# Block diagram level 1 drawio
│	│   ├── bpmn/
│	│	│   ├── l1.drawio  		# BPMN diagram level 1 drawio
│	│	│   ├── l1.drawio.png  	# BPMN diagram level 1 drawio
│	│	│   ├── l2.drawio  		# BPMN diagram level 2 drawio
│	│	│   ├── l2.drawio.png  	# BPMN diagram level 2 drawio
│	│	│   ├── l3.drawio  		# BPMN diagram level 3 drawio
│	│	│   ├── l3.drawio.png  	# BPMN diagram level 3 drawio
│	│   ├── fc/
│	│	│   ├── l1.drawio  		# FC diagram level 1 drawio
│	│	│   ├── l1.drawio.png  	# FC diagram level 1 drawio
│	│	│   ├── l2.drawio  		# FC diagram level 2 drawio
│	│	│   ├── l2.drawio.png  	# FC diagram level 2 drawio
│	│	│   ├── l3.drawio  		# FC diagram level 3 drawio
│	│	│   ├── l3.drawio.png  	# FC diagram level 3 drawio
│ 	+
├── models/						# Models Information (technical report)
├── problems/					# Problems Information (definition, solution, original and official test cases)
├── results/human_eval			# Results obtained
├── src/
│   ├── core/               	# Core functionality (model management, code execution, GPU utilities)
│   ├── ui/                 	# Gradio interface and styles
│   ├── utils/              	# Shared constants and utilities
├── main.py                 	# Application entry point
├── requirements.txt        	# Project dependencies
└── README.md               	# Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/carlodenardin/svlm.git
   cd project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Available Models

| Model            | Size / Variant          | Notes / Purpose | Link |
|------------------|-------------------------|-----------------|------|
| **Gemma 3**      | 4B / 4B 4bit (quantized) | Multimodal transformer with SigLIP vision encoder | [Gemma 4B](https://huggingface.co/google/gemma-3-4b-it) / [4bit](https://huggingface.co/unsloth/gemma-3-4b-it-bnb-4bit) |
| **PaliGemma 2**  | 3B Mix                  | Lightweight VLM for captioning / OCR / description | [PaliGemma 2](https://huggingface.co/google/paligemma2-3b-mix-448) |
| **LLaVA 1.5**    | 7B 4bit (quantized)     | Open-source multimodal (LLaMA/Vicuna-based) | [LLaVA 1.5](https://huggingface.co/unsloth/llava-1.5-7b-hf-bnb-4bit) |
| **MiniCPM V4**   | 4.1B                    | On-device multimodal model with SigLIP2 | [MiniCPM V4](https://huggingface.co/openbmb/MiniCPM-V-4) |
| **LFM2-VL**      | 450M / 1.6B             | Lightweight multimodal models optimized for edge devices | [450M](https://huggingface.co/LiquidAI/LFM2-VL-450M) / [1.6B](https://huggingface.co/LiquidAI/LFM2-VL-1.6B) |
| **Perception LM**| 1B                      | Open MLLM for detailed image/video understanding | [Perception LM 1B](https://huggingface.co/facebook/Perception-LM-1B) |
| **GPT-5-nano**   | ~120B (5B active)       | Used as reliable benchmark (API required in env) | - |

🖥️ **Hardware Note**  
All the small vision-language models listed above were successfully run on a **single NVIDIA RTX 5080ti**, without requiring special optimizations.

## Gradio Interface

![alt text](https://raw.githubusercontent.com/carlodenardin/svlm/refs/heads/main/gradio.png)
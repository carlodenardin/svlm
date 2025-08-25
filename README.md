# Small Vision Language Model - Image Text to Code

This project investigates the capability of small vision-language models (SVLMs) to generate functional code by interpreting algorithmic diagrams. The core question is whether a small model can look at a diagram and produce correct, executable Python code.

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

## The Setup

The evaluation uses a subset of **10 problems** from the **HumanEval**. For each problem, a set of diagrams was created to serve as the models' input:
* Flowcharts (3 levels of detail)
* BPMN diagrams (3 levels of detail)
* Block diagrams (1 level of detail)

The methodology involves two primary tests:

1.  **Direct Code Generation**: The model receives only a diagram and must generate a Python function. The output is then validated against a balanced test dataset to determine its **Acceptance Rate**.
2.  **Reasoning Test**: This two-step process first prompts the SVLM to explain the diagram's logic in plain English. This text-based reasoning is then passed to a more powerful model (GPT-5-nano) to generate the final code. This test assesses whether the SVLM correctly understood the algorithm, separate from its ability to write code.


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

## Results

* **Gemma 3 4B** (and its 4-bit quantized version) achieved solid results, proving suitable for this kind of task.
* **MiniCPM V 4.0**, designed for on-device use, shows promising capabilities.
* **LLaVA** and **PaliGemma** were found to be unsuitable for this task, likely because they are designed for different use cases like image captioning.
* As diagram complexity and detail level increase, model performance generally decreases.
* Some of the smallest models, like **LFM2 VL**, demonstrate a surprising ability to *explain* the algorithm's logic but often fail at basic implementation details, such as using `print` instead of `return` or getting stuck in infinite loops.

Other results and visualization will provided in the next days.


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

In the next days implementation for bulk tests will be provided. Use gradio for on fly tests. GPT requires the API in the env file

## Gradio Interface

![alt text](https://raw.githubusercontent.com/carlodenardin/svlm/refs/heads/main/gradio.png)
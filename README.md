# Small Vision Language Model - Image Text to Code

This project provides a benchmark for evaluating multimodal models in the task of code generation from graphical representations, using datasets from Human-Eval and PSB2.

## Project Structure
```
project/
├── src/
│   ├── core/               # Core functionality (model management, code execution, GPU utilities)
│   ├── data/               # Data loading and processing
│   ├── ui/                 # Gradio UI components and main interface
│   ├── utils/              # Shared constants and utilities
├── main.py                 # Application entry point
├── css/                    # Custom CSS for Gradio interface
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
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

## Usage
- **Home Tab**: View problem details, solutions, test cases, and diagrams for Human-Eval and PSB2 datasets.
- **On-The-Fly Test Tab**: Load a model, select a problem and diagram, and generate code responses interactively.
- **Bulk Test Tab**: Run automated tests across multiple problems, diagram types, and levels.

## Requirements
See `requirements.txt` for a list of dependencies.

## Notes
- Ensure a compatible GPU is available for model inference.
- The `MODEL_MAP` in `src/utils/const.py` must be configured with appropriate model IDs.
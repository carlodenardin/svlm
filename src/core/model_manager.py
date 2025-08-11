import torch
from transformers import AutoProcessor, AutoModelForCausalLM, LlavaForConditionalGeneration
from src.utils.const import MODEL_MAP
from PIL import Image
import accelerate  # Explicit import to ensure detection

class ModelManager:
    def __init__(self):
        self.current_model = None
        self.model_name = None
        self.model = None
        self.processor = None

    def load_model(self, model_name):
        """
        Load the specified model.
        """
        if self.current_model:
            self.unload_model()
        
        if model_name not in MODEL_MAP:
            return f"Model {model_name} not found in MODEL_MAP"
        
        config = MODEL_MAP[model_name]
        try:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            if model_name == "MiniCPM-V-4":
                self.processor = AutoProcessor.from_pretrained(config["model"])
                self.model = AutoModelForCausalLM.from_pretrained(
                    config["model"],
                    torch_dtype=torch.float16,
                    device_map="auto" if torch.cuda.is_available() else None
                )
            elif model_name == "llava":
                self.processor = AutoProcessor.from_pretrained(config["model"])
                self.model = LlavaForConditionalGeneration.from_pretrained(
                    config["model"],
                    torch_dtype=torch.float16,
                    low_cpu_mem_usage=True,
                    load_in_4bit=True,
                    device_map="auto" if torch.cuda.is_available() else None
                )
            else:
                return f"Unsupported model: {model_name}"
            
            self.model_name = model_name
            self.current_model = config["model"]
            return f"Loaded {config['name']} successfully"
        except Exception as e:
            return f"Error loading model {model_name}: {str(e)}"
        finally:
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

    def unload_model(self):
        """
        Unload the current model to free memory.
        """
        if self.model:
            del self.model
            self.model = None
        if self.processor:
            del self.processor
            self.processor = None
        self.current_model = None
        self.model_name = None
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        return "Model unloaded successfully"

    def generate_response(self, image_input, prompt):
        """
        Generate a response using the loaded model.
        """
        if not self.current_model:
            return "No model loaded. Please load a model first."
        
        try:
            config = MODEL_MAP[self.model_name]
            device = "cuda" if torch.cuda.is_available() else "cpu"
            if self.model_name == "MiniCPM-V-4":
                inputs = self.processor(images=image_input, text=prompt, return_tensors="pt").to(device, torch.float16)
                output = self.model.generate(**inputs, max_new_tokens=config["max_tokens"], do_sample=False)
                response = self.processor.decode(output[0], skip_special_tokens=True).strip()
            elif self.model_name == "llava":
                conversation = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": f"Generate Python code to solve the following problem based on this diagram:\n{prompt}"},
                            {"type": "image"}
                        ]
                    }
                ]
                llava_prompt = self.processor.apply_chat_template(conversation, add_generation_prompt=True)
                inputs = self.processor(images=image_input, text=llava_prompt, return_tensors="pt").to(device, torch.float16)
                output = self.model.generate(**inputs, max_new_tokens=config["max_tokens"], do_sample=False)
                response = self.processor.decode(output[0][2:], skip_special_tokens=True).strip()
            else:
                return f"Unsupported model: {self.model_name}"
            
            # Clean markdown code fences
            if response.startswith("```python") and response.endswith("```"):
                response = response[9:-3].strip()
            elif response.startswith("```") and response.endswith("```"):
                response = response[3:-3].strip()
            
            return response
        except Exception as e:
            return f"Error generating response: {str(e)}"
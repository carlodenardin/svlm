from src.core.models.base_model import BaseModel
from transformers import AutoProcessor, AutoModelForImageTextToText

import torch

class LFM21B(BaseModel):
    
    def load(self):
        try:

            self.processor = AutoProcessor.from_pretrained(
                self.model_config['model'],
                trust_remote_code = True
            )

            self.model = AutoModelForImageTextToText.from_pretrained(
                self.model_config['model'],
                device_map = self.device,
                torch_dtype = torch.bfloat16,
                trust_remote_code = True
            ).eval()

            return f"Loaded {self.model_config['name']}."
        
        except Exception as e:
            return f"Error: {str(e)}"
        
    def generate_response(self, image_input, prompt):
        try:
            conversation = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": image_input},
                        {"type": "text", "text": prompt}
                    ]
                },
            ]

            inputs = self.processor.apply_chat_template(
                conversation,
                add_generation_prompt = True,
                tokenize = True,
                return_dict = True,
                return_tensors = "pt",
            ).to(self.model.device, dtype = torch.bfloat16)

            with torch.inference_mode():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens = 512,
                    do_sample = False
                )

            response = self.processor.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens = True)

            return response
        except Exception as e:
            return f"Error generating response: {str(e)}"
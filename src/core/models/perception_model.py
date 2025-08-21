from src.core.models.base_model import BaseModel
from transformers import AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig

import torch

class PerceptionModel(BaseModel):

    def load(self):
        try:
            quantization_config = BitsAndBytesConfig(
                load_in_8bit = True,
                bnb_8bit_compute_dtype = torch.bfloat16,
                bnb_8bit_use_double_quant = True
            )

            self.processor = AutoProcessor.from_pretrained(
                self.model_config['model'],
                use_fast = True
            )
            self.model = AutoModelForImageTextToText.from_pretrained(
                self.model_config['model'],
                quantization_config=quantization_config,
                device_map = self.device
            )
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
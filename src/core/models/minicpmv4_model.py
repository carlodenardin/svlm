from src.core.models.base_model import BaseModel
from transformers import AutoProcessor, AutoModelForCausalLM

import torch

class MiniCPMV4Model(BaseModel):

    def load(self):
        try:
            self.processor = AutoProcessor.from_pretrained(
                self.model_config['model'],
                use_fast = False,
                trust_remote_code = True
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_config['model'],
                device_map = self.device,
                trust_remote_code = True,
                torch_dtype = torch.float16,
            )
            return f"Loaded {self.model_config['name']}."
        except Exception as e:
            return f"Error: {str(e)}"
        
    def generate_response(self, image_input, prompt):
        try:
            inputs = self.processor(images = image_input, text = prompt, return_tensors = "pt").to(self.model_config, torch.float16)
            output = self.model.generate(**inputs, max_new_tokens = 512, do_sample = False)
            response = self.processor.decode(output[0], skip_special_tokens = True).strip()

            return response
        except Exception as e:
            return f"Error generating response: {str(e)}"
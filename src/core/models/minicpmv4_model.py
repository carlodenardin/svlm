from src.core.models.base_model import BaseModel
from transformers import AutoTokenizer, AutoModel
from PIL import Image

import torch

class MiniCPMV4Model(BaseModel):

    def load(self):
        try:

            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_config['model'],
                trust_remote_code = True
            )

            self.model = AutoModel.from_pretrained(
                self.model_config['model'],
                device_map = self.device,
                trust_remote_code = True,
                attn_implementation='sdpa',
                torch_dtype=torch.bfloat16
            )

            return f"Loaded {self.model_config['name']}."
        except Exception as e:
            return f"Error: {str(e)}"
        
    def generate_response(self, image_input, prompt):
        try:

            conversation = [{'role': 'user', 'content': [image_input.convert("RGB"), prompt]}]

            answer = self.model.chat(
                msgs = conversation,
                image = image_input,
                tokenizer = self.tokenizer
            )
   
            return answer
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return f"Error generating response: {str(e)}"
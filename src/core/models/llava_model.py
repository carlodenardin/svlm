import torch

from transformers import AutoProcessor, LlavaForConditionalGeneration
from .base_model import BaseModel

class LlavaModel(BaseModel):
    
    def load(self):
        try:

            self.processor = AutoProcessor.from_pretrained(
                self.model_config['model'],
                use_fast = False,
            )

            self.model = LlavaForConditionalGeneration.from_pretrained(
                self.model_config['model'],
                device_map = self.device,
                low_cpu_mem_usage = True,
                torch_dtype = torch.float16,
            ).to(self.device)

            return f"Loaded {self.model_config['name']}."
        
        except Exception as e:
            return f"Error: {str(e)}"
        
    def generate_response(self, image_input, prompt):
        try:
            conversation = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image"}
                    ]
                }
            ]

            llava_pompt = self.processor.apply_chat_template(conversation, add_generation_prompt = True)
            inputs = self.processor(images = image_input, text = llava_pompt, return_tensors = "pt").to(self.device, torch.float16)
            output = self.model.generate(**inputs, max_new_tokens = 512, do_sample = False)
            response = self.processor.decode(output[0][2:], skil_special_tokens = True).strip()

            return response
        except Exception as e:
            return f"Error generating response: {str(e)}"
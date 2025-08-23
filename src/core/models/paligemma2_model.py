from src.core.models.base_model import BaseModel
from transformers import PaliGemmaProcessor, PaliGemmaForConditionalGeneration

import torch

class PaliGemma2Model(BaseModel):

    def load(self):
        try:
            self.processor = PaliGemmaProcessor.from_pretrained(
                self.model_config['model'],
                use_fast = True
            )

            self.model = PaliGemmaForConditionalGeneration.from_pretrained(
                self.model_config['model'],
                device_map = self.device,
                torch_dtype = torch.bfloat16,
            ).eval()

            return f"Loaded {self.model_config['name']}."
        
        except Exception as e:
            return f"Error: {str(e)}"
        
    def generate_response(self, image_input, prompt):

        try:

            inputs = self.processor(
                text = f"<image> {prompt}",
                images = image_input.convert("RGB"),
                return_tensors = "pt",
            ).to(self.model.device, dtype = torch.bfloat16)

            input_len = inputs["input_ids"].shape[-1]

            with torch.inference_mode():
                generation = self.model.generate(**inputs, max_new_tokens = 512, do_sample = False)
                generation = generation[0][input_len:]
                response = self.processor.decode(generation, skip_special_tokens = True)

            return response
        except Exception as e:
            return f"Error generating response: {str(e)}"
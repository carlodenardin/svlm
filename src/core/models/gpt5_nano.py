from src.core.models.base_model import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

import base64
import os
import io

load_dotenv()
api_key = os.getenv("GPT5_NANO")



class GPT5NanoModel(BaseModel):

    def _encode_image(self, image):
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        return base64.b64encode(img_bytes).decode("utf-8")

    def load(self):
        if api_key is not None:
            self.client = OpenAI(api_key = api_key)
            return "Model loaded (using OpenAI API)"
        return "Define OpenAI API in env"
        
    def generate_response(self, image_input, prompt):
        if image_input is not None:
            response = self.client.responses.create(
                model = self.model_config["model"],
                input=[
                    {
                        "role": "user",
                        "content": [
                            { "type": "input_text", "text": prompt },
                            {
                                "type": "input_image",
                                "image_url": f"data:image/png;base64,{self._encode_image(image_input)}",
                            },
                        ],
                    }
                ],
            )
        else:
            response = self.client.responses.create(
                model = self.model_config["model"],
                input=[
                    {
                        "role": "user",
                        "content": [
                            { "type": "input_text", "text": prompt },
                        ],
                    }
                ],
            )

        return response.output_text;


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
        # Create a byte buffer in memory
        buffered = io.BytesIO()
        # Save the image object to the buffer in PNG format
        image.save(buffered, format="PNG")
        # Get the bytes from the buffer and encode them
        img_bytes = buffered.getvalue()
        return base64.b64encode(img_bytes).decode("utf-8")

    def load(self):
        if api_key is not None:
            self.client = OpenAI(api_key = api_key)
            return "Model loaded (using OpenAI API)"
        return "Define OpenAI API in env"
        
    def generate_response(self, image_input, prompt):

        response = self.client.responses.create(
            model="gpt-4.1",
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

        return response.output_text;


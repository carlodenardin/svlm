from abc import ABC, abstractmethod
import torch

class BaseModel(ABC):
    def __init__(self, model_config):
        self.model_config = model_config
        self.model = None
        self.processor = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def generate_response(self, image_input, prompt):
        pass

    def unload(self):
        del self.model
        del self.processor
        self.model = None
        self.processor = None

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        
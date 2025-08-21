from src.utils.const import MODEL_MAP

class ModelManager:
    def __init__(self):
        self.current_model = None
        self.model_name = None

    def load_model(self, model_name):
        if self.current_model:
            self.unload_model()
        
        if model_name not in MODEL_MAP:
            return f"Unavailable model."
        
        try:
            model_info = MODEL_MAP[model_name]
            model_class = model_info["class"]
            self.current_model = model_class(model_info)
            self.model_name = model_name
            return self.current_model.load()
        except Exception as e:
            return f"Error loading model {model_name}: {str(e)}"

    def unload_model(self):
        if self.current_model:
            self.current_model.unload() 
            del self.current_model
            self.current_model = None
            self.model_name = None

        return "Model unloaded."
    
    def generate_response(self, image_input, prompt):
        if not self.current_model:
            return "Load a model."
        
        return self.current_model.generate_response(image_input, prompt)
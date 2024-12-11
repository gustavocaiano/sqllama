import requests
import json

class LlamaChat:
    def __init__(self, model_name="qwen2.5"):
        self.model_name = model_name
        self.base_url = "http://localhost:11434/api"
        self.schema = None
        
    def generate_response(self, prompt):
        url = f"{self.base_url}/generate"
        
        # Se o schema já foi definido, incluímos ele no contexto
        if self.schema:
            context = f"Database Schema:\n{self.schema}\n\nUser Question: {prompt}\n\nRespond only with a SELECT query or ask for clarification if the question is not clear enough. Do not provide any additional explanation. If the 'User Question:' Is not Followed by a question, Ask for a question. If, in order to answer correctly , you need to use another syntax besides SELECT, please warn the user first and tell them not to run the query."
        else:
            context = prompt
            
        data = {
            "model": self.model_name,
            "prompt": context,
            "stream": False
        }
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()['response']
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
    
    def set_schema(self, schema):
        self.schema = schema
        return "OK"
        
    def load_schema_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                schema = file.read()
            self.schema = schema
            return "Schema loaded successfully"
        except Exception as e:
            return f"Error loading schema: {str(e)}" 

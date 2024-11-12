from llama_cpp import Llama

def load_llama_model(model_path):
    return Llama(model_path=model_path)



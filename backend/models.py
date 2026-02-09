import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_model(model_name: str, prompt: str) -> str:
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]

def llama_process(text: str) -> str:
    return run_model(
        "llama3",
        f"You are a historian AI. Clean and modernize this text:\n{text}"
    )

def deepseek_process(text: str) -> str:
    return run_model(
        "deepseek-r1",
        f"Correct spelling and preserve meaning:\n{text}"
    )

def qwen_process(text: str) -> str:
    return run_model(
        "qwen2.5",
        f"Rewrite clearly but keep historical accuracy:\n{text}"
    )

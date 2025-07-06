import requests

def run_llama(prompt: str) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",  # Update if using different port or endpoint
            json={"model": "llama3", "prompt": prompt}
        )
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"LLaMA Error: {str(e)}"

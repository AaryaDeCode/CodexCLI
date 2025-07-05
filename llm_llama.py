import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def ask_llama(question, context_snippets):
    context = "\n\n".join(
        f"File: {s['path']} (around line {s['line_start']})\n{s['snippet']}"
        for s in context_snippets
    )

    prompt = f"""You are a helpful AI assistant. A developer is asking a question about the codebase. Use the provided code snippets to answer precisely.

Mention relevant file names and line numbers.

Question:
{question}

Code Snippets:
{context}
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })

        if response.ok:
            return response.json().get("response", "").strip()
        else:
            return f"❌ LLaMA error (status {response.status_code}): {response.text}"
    except requests.exceptions.RequestException as e:
        return f"❌ Connection error: {e}"

def generate_keywords(question):
    prompt = f"""You're an AI assistant. Given the following developer question, return 6-10(as many as you can) keywords or variable names that would help locate the answer in a codebase.

Return as comma-separated values (no explanation).

Question:
{question}
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })

        if response.ok:
            text = response.json().get("response", "")
            return [k.strip() for k in text.split(",") if k.strip()]
        else:
            return []
    except requests.exceptions.RequestException:
        return []

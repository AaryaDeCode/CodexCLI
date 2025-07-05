# 🧠 Codebase-Aware AI Assistant (Terminal Version)

A terminal-based AI assistant that lets you interact with any GitHub codebase using natural language.

Just give it a GitHub URL — it will:
- Clone the repo
- Analyze the code using BERT (semantic search)
- Generate search keywords with LLaMA 3
- Answer your technical questions using LLaMA 3

## ✨ Features

- 🔍 **Keyword + Semantic Search**: Combines BERT embeddings + LLaMA keywords to find relevant code.
- 🤖 **AI Answers via LLaMA 3**: Answers questions like “Where is the database connection?”, “What model is used?”.
- 🧠 **Automatic Keyword Generation**: Converts your query into smart search terms using LLaMA.
- 🧾 **Terminal Interface**: Fully interactive via CLI — no GUI required.

## 📦 Tech Stack

- Python 3.8+
- [Ollama](https://ollama.com/) + LLaMA 3 (for local AI inference)
- SentenceTransformers (`all-MiniLM-L6-v2`) for semantic embedding
- GitPython for repo cloning

## 🚀 How to Run

### 1. Install Ollama and Pull LLaMA 3

```bash
ollama run llama3
````

> Make sure Ollama is running at `http://localhost:11434`

---

### 2. Clone and Install Dependencies

```bash
git clone https://github.com/yourname/codebase-ai-assistant.git
cd codebase-ai-assistant
pip install -r requirements.txt
```

---

### 3. Run the Assistant

```bash
python main.py
```

You’ll be prompted to:

1. Enter a GitHub repo URL
2. Ask questions like:

   * `Where is the database connection configured?`
   * `Which LLM is used in this code?`
   * `What does the predict_log() function do?`

---

## 🧪 Example

```bash
🔗 Enter GitHub repo URL:
> https://github.com/example/repo.git

📂 Indexing codebase...

💬 Ask questions about the codebase. Type 'exit' to quit.

You: where is the LLM used?
🧠 Keywords: ['llm', 'ollama_model', 'model']

🤖 LLaMA 3:
The project uses LLaMA 3 via the variable OLLAMA_MODEL = "llama3" in llm_llama.py, around line 3.
```

---

## 📁 Folder Structure

```
.
├── main.py
├── code_cloner.py
├── code_indexer.py
├── search_engine.py
├── llm_llama.py
├── requirements.txt
├── README.md
└── temp_repos/
```

---



---

## 🙋‍♂️ Credits

Built by \[Your Name] — inspired by the idea of “ChatGPT for your codebase”.

Model: [LLaMA 3 by Meta](https://ollama.com/library/llama3)
Embeddings: [SentenceTransformers](https://www.sbert.net/)

---






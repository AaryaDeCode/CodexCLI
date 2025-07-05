import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def index_codebase(repo_path):
    files_data = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((
                ".py", ".js", ".ts", ".java", ".go", ".rb", ".json",
                ".yml", ".yaml", ".ipynb", ".md", ".env", ".toml"
            )):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        chunks = split_into_chunks(content, 20)  # 20 lines per chunk
                        for idx, chunk in enumerate(chunks):
                            embedding = model.encode(chunk)
                            files_data.append({
                                "path": full_path,
                                "line_start": idx * 20 + 1,
                                "snippet": chunk,
                                "embedding": embedding
                            })
                except Exception as e:
                    print(f"⚠️ Skipped {full_path}: {e}")
    return files_data

def split_into_chunks(text, lines_per_chunk=20):
    lines = text.splitlines()
    chunks = []
    for i in range(0, len(lines), lines_per_chunk):
        chunk = "\n".join(lines[i:i+lines_per_chunk])
        if chunk.strip():
            chunks.append(chunk)
    return chunks

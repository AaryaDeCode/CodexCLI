from code_cloner import clone_repo
from code_indexer import index_codebase
from search_engine import hybrid_search
from llm_llama import ask_llama, generate_keywords

def main():
    print("🔗 Enter GitHub repo URL:")
    url = input("> ")

    repo_path = clone_repo(url)
    print(f"✅ Repo cloned to: {repo_path}")

    print("📂 Indexing codebase...")
    indexed_chunks = index_codebase(repo_path)

    print("\n💬 Ask questions about the codebase. Type 'exit' to quit.")
    while True:
        query = input("\nYou: ")
        if query.lower() == "exit":
            break

        keywords = generate_keywords(query)
        print(f"🧠 Keywords: {keywords}")

        snippets = hybrid_search(query, keywords, indexed_chunks)
        if not snippets:
            print("❌ No relevant code found.")
            continue

        answer = ask_llama(query, snippets)
        print(f"\n🤖 LLaMA 3:\n{answer}\n")

if __name__ == "__main__":
    main()

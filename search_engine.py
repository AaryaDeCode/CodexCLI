from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def hybrid_search(query, keywords, indexed_chunks, top_k=5):
    query_vec = model.encode(query)
    scored_chunks = []

    # Step 1: Semantic Search
    for chunk in indexed_chunks:
        sim = cosine_similarity([query_vec], [chunk["embedding"]])[0][0]
        if sim > 0.3:  # filter weak matches
            scored_chunks.append((sim, chunk))

    # Step 2: Keyword Boosting (adds weak-scored chunks if they match)
    for chunk in indexed_chunks:
        match = any(k.lower() in chunk["snippet"].lower() for k in keywords)
        if match:
            key = chunk["path"] + str(chunk["line_start"])
            if not any(key == (c["path"] + str(c["line_start"])) for _, c in scored_chunks):
                scored_chunks.append((0.31, chunk))  # weak boost for keyword match

    # ✅ FIXED: Sort by score (first item in tuple)
    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    # Step 3: Return top unique results
    seen = set()
    results = []
    for sim, chunk in scored_chunks:
        key = chunk["path"] + str(chunk["line_start"])
        if key not in seen:
            seen.add(key)
            results.append({
                "path": chunk["path"],
                "line_start": chunk["line_start"],
                "snippet": chunk["snippet"],
                "score": round(sim, 3)
            })
        if len(results) >= top_k:
            break

    return results

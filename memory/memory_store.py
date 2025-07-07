# memory/memory_store.py

import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Init embedding and chroma
embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection(name="dataset_queries", embedding_function=embedding_fn)

model = SentenceTransformer('all-MiniLM-L6-v2')

def check_memory(prompt, threshold=0.3):
    query_embedding = model.encode(prompt).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1,
        include=["distances", "documents"]
    )

    if not results.get("documents") or not results["documents"][0]:
        return None

    distance = results["distances"][0][0]
    print(f"[Memory Check] Distance: {distance}")

    if distance >= threshold:
        return None

    return results["documents"][0]



def save_to_memory(query, results):
    normalized_id = query.lower().strip().replace(" ", "_")
    collection.add(
        documents=[results],
        metadatas=[{"cached": True}],
        ids=[normalized_id]
    )


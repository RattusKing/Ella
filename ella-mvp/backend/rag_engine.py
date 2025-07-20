# Retrieval-Augmented Generation (RAG) logic
# rag_engine.py
# Handles retrieval-augmented generation (RAG) using local documents.

import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Paths
VECTOR_STORE_PATH = "data/vector_store/faiss_index"
DOC_PATH = "data/knowledge/"

# Load embedding model (offline compatible)
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # Fast + decent quality

# Load FAISS index
def load_index():
    index_file = os.path.join(VECTOR_STORE_PATH, "index.faiss")
    meta_file = os.path.join(VECTOR_STORE_PATH, "index.pkl")

    if not os.path.exists(index_file) or not os.path.exists(meta_file):
        print("FAISS index not found. Please run ingest_knowledge.py first.")
        return None, []

    index = faiss.read_index(index_file)
    with open(meta_file, "rb") as f:
        documents = pickle.load(f)

    return index, documents

# Search index and return top matches
def retrieve_context(query, top_k=3):
    index, documents = load_index()
    if index is None:
        return "No context available."

    query_embedding = embedder.encode([query])
    D, I = index.search(query_embedding, top_k)

    results = [documents[i] for i in I[0] if i < len(documents)]
    return "\n---\n".join(results)

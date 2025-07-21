# Script to load and vectorize documents
import os
import glob
import pickle
import faiss
from sentence_transformers import SentenceTransformer

# Paths
DOCS_PATH = "data/knowledge/"
VECTOR_STORE_PATH = "data/vector_store/faiss_index/"
INDEX_FILE = os.path.join(VECTOR_STORE_PATH, "index.faiss")
META_FILE = os.path.join(VECTOR_STORE_PATH, "index.pkl")

# Create vector store directory if not exists
os.makedirs(VECTOR_STORE_PATH, exist_ok=True)

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight and fast

def load_documents():
    docs = []
    for filepath in glob.glob(os.path.join(DOCS_PATH, "*.md")) + glob.glob(os.path.join(DOCS_PATH, "*.txt")):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            docs.append(content)
    return docs

def embed_documents(docs):
    print(f"Embedding {len(docs)} documents...")
    embeddings = embedder.encode(docs, show_progress_bar=True)
    return embeddings

def build_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def save_index_and_meta(index, docs):
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(docs, f)
    print(f"Saved FAISS index to {INDEX_FILE} and metadata to {META_FILE}")

def main():
    documents = load_documents()
    if not documents:
        print("No documents found in knowledge folder.")
        return

    embeddings = embed_documents(documents)
    index = build_faiss_index(embeddings)
    save_index_and_meta(index, documents)

if __name__ == "__main__":
    main()

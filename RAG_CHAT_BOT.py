from app.loader import load_documents
from app.chunker import chunk_text
from app.embedder import embed_texts
from app.vectordb import store_embeddings

docs = load_documents("data/documents")
chunks = []
for d in docs:
    chunks.extend(chunk_text(d))

embeddings = embed_texts(chunks)
store_embeddings(embeddings, chunks)

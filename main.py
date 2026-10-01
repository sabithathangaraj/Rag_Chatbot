from app.loader import load_documents
from app.chunker import chunk_text
from app.embedder import embed_texts
from app.vectordb import store_embeddings


def main():
    # 1️⃣ Load documents
    docs = load_documents("data/documents")

    # 2️⃣ Chunk documents
    chunks = []
    for d in docs:
        chunks.extend(chunk_text(d))

    # 3️⃣ Create embeddings
    embeddings = embed_texts(chunks)

    # 4️⃣ Store in vector database
    store_embeddings(embeddings, chunks)

    print("✅ Data successfully stored in vector DB!")


if __name__ == "__main__":
    main()
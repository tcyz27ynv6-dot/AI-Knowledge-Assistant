import json
import chromadb
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

print("Loading chunks...")
with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

client = chromadb.PersistentClient(path="./vector_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)

for chunk in chunks:

    embedding = model.encode(
        chunk["text"]
    ).tolist()

    collection.add(
        ids=[chunk["id"]],
        documents=[chunk["text"]],
        embeddings=[embedding],
        metadatas=[
            {
                "source": chunk["source"]
            }
        ]
    )

print("Embeddings stored successfully!")

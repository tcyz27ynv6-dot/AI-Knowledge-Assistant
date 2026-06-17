import chromadb
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_collection(
    "knowledge_base"
)

question = input("Ask a question: ")

query_embedding = model.encode(
    question
).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

print("\nSearch Results:\n")

for doc in results["documents"][0]:
    print(doc)
    print("-" * 50)
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_collection(
    "knowledge_base"
)

question = "What is FloCard?"

query_embedding = model.encode(
    question
).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print(results["documents"])


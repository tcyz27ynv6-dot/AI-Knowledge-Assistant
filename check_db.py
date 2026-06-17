import chromadb

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_collection(
    "knowledge_base"
)

print(
    "Total Chunks:",
    collection.count()
)
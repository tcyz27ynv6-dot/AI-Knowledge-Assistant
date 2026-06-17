import chromadb

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_collection(
    "knowledge_base"
)

data = collection.get()

sources = set()

for metadata in data["metadatas"]:
    sources.add(
        metadata["source"]
    )

print(sources)

import chromadb

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_collection(
    "knowledge_base"
)

data = collection.get()

ids_to_delete = []

files_to_remove = [
    "sales.pdf",
    "Quotation For Waterproofing  3.pdf",
    "NewSyllabus_96849859-5c25-4f90-9f68-95475041b7f2.pdf"
]

for i in range(len(data["ids"])):

    metadata = data["metadatas"][i]

    if metadata["source"] in files_to_remove:

        ids_to_delete.append(
            data["ids"][i]
        )

print(
    "Chunks found:",
    len(ids_to_delete)
)

if ids_to_delete:

    collection.delete(
        ids=ids_to_delete
    )

    print(
        "Files removed successfully."
    )

else:

    print(
        "No matching files found."
    )
import chromadb
import json
import os
import time
from datetime import datetime
from sentence_transformers import SentenceTransformer
import ollama

print("Loading model...")

embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

client = chromadb.PersistentClient(path="./vector_db")

collection = client.get_or_create_collection("knowledge_base")


def ask_rag(question):
    start_time = time.time()

    query_embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    latency = round(time.time() - start_time, 2)

    log_entry = {
        "time": str(datetime.now()),
        "question": question,
        "latency_seconds": latency,
        "retrieved_chunk_ids": results["ids"][0],
        "sources": results["metadatas"][0]
    }

    os.makedirs("LOGS", exist_ok=True)

    with open("LOGS/query_logs.txt", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return {
        "answer": response["message"]["content"],
        "sources": results["metadatas"][0],
        "documents": results["documents"][0],
        "retrieved_chunk_ids": results["ids"][0],
        "latency_seconds": latency
    }

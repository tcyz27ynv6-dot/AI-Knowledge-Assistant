from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

text = "What is FloCard?"

embedding = model.encode(text)

print("Embedding length:", len(embedding))

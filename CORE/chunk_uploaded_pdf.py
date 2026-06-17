import json

with open(
    "DATA/uploaded_pdf.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()

words = content.split()

chunk_size = 30

chunks = []

for i in range(0, len(words), chunk_size):

    chunk_text = " ".join(
        words[i:i + chunk_size]
    )

    chunks.append({
        "id": f"pdf_chunk_{len(chunks)+1}",
        "text": chunk_text,
        "source": "uploaded_pdf"
    })

with open(
    "DATA/pdf_chunks.json",
    "w",
    encoding="utf-8"
) as outfile:

    json.dump(
        chunks,
        outfile,
        indent=4
    )

print(
    f"{len(chunks)} chunks created!"
)
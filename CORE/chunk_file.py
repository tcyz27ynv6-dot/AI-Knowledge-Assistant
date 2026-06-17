import json
import os

chunks = []
chunk_size = 30

data_folder = "DATA"

for filename in os.listdir(data_folder):

    if filename.endswith(".md"):

        filepath = os.path.join(
            data_folder,
            filename
        )

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        words = content.split()

        for i in range(
            0,
            len(words),
            chunk_size
        ):

            chunk_words = words[
                i:i + chunk_size
            ]

            chunk_text = " ".join(
                chunk_words
            )

            chunks.append({
                "id": f"chunk_{len(chunks)+1}",
                "text": chunk_text,
                "source": filename
            })

with open(
    "DATA/chunks.json",
    "w",
    encoding="utf-8"
) as outfile:

    json.dump(
        chunks,
        outfile,
        indent=4
    )

print(
    f"{len(chunks)} chunks created successfully!"
)


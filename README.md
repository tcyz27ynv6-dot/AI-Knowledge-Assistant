AI Knowledge Assistant

Overview

AI Knowledge Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to upload documents, ask questions, and receive answers with citations.

Features
	•	PDF Upload
	•	DOCX Upload
	•	CSV Upload
	•	Markdown Upload
	•	ChromaDB Vector Database
	•	Semantic Search
	•	Ollama Llama 3.1 Integration
	•	Word Export
	•	Excel Export
	•	Query Logging
	•	Latency Tracking

Tech Stack
	•	FastAPI
	•	Next.js
	•	ChromaDB
	•	Ollama
	•	Llama 3.1
	•	Sentence Transformers

Architecture

Documents
→ Ingestion
→ Chunking
→ Embeddings
→ ChromaDB
→ Retrieval
→ Ollama
→ FastAPI
→ Next.js UI

Run Backend

uvicorn API.main:app –reload

Run Frontend

cd frontend

npm install

npm run dev

Author

Akshita Prakash
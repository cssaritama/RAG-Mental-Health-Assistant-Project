# Architecture Overview

Components:
- Ingestion: cleaning & chunking
- Vector store: FAISS or in-memory (example provided)
- Retrieval: simple vs hybrid, reranking
- LLM: prompt templates & evaluation harness
- Interface: Streamlit app with feedback
- Monitoring: dashboard + feedback CSV

# Mental Health RAG Assistant

End-to-end Retrieval-Augmented Generation (RAG) project built for the DataTalksClub LLM Zoomcamp certification.
This repository implements ingestion, retrieval (hybrid), LLM prompting, evaluation, UI, monitoring and containerization.

## Key features
- Problem: Provide trustworthy, non-diagnostic mental health information sourced from reliable documents.
- Ingestion: automated Python script to load, clean and chunk documents.
- Retrieval: hybrid (keyword + vector) + re-ranking and query rewriting.
- LLM: prompt templates and evaluation harness (mocked LLM for reproducibility).
- Interface: Streamlit UI with feedback collection.
- Monitoring: Streamlit dashboard + feedback CSV; placeholders for 5+ charts.
- Containerization: Dockerfile and docker-compose for reproducible deployment.
- Tests: basic unit tests and evaluation scripts.

## Quickstart (local)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python ingestion/ingest_data.py --source data/raw --output data/processed
streamlit run interface/app.py
```

See `docs/` for details on architecture and evaluation methodology.


## Evaluation scripts

Run retrieval evaluation:
```
python evaluation/retrieval_evaluation.py
```

Run LLM evaluation:
```
python evaluation/llm_evaluation.py
```

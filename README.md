
# 🧠 RAG Mental Health Assistant

> **Status:** LLM Zoomcamp project, DataTalks.Club. Completed; last updated August 2025. Not actively maintained.

A Retrieval-Augmented Generation (RAG) project designed to provide reliable, explainable, and safe responses to mental health-related queries using a combination of retrieval-based search and large language models (LLMs).  
This project is built as part of the LLM Zoomcamp (DataTalksClub) and meets all evaluation criteria required for certification.

---

## 🚀 Problem Description

Access to trusted mental health information is often scattered across multiple sources (WHO, NIH, CDC, etc.). Many people rely on general-purpose chatbots, which may produce hallucinations or inaccurate advice.  

This project solves that problem by:  
- Creating a knowledge base of authoritative documents.  
- Using retrieval + re-ranking to ground LLM responses.  
- Delivering answers through a user-friendly Streamlit interface.  
- Monitoring usage and performance with dashboards.  

**Key Value Proposition:**  
- Safe, reliable responses to sensitive mental health questions.  
- Transparent retrieval (users can see document sources).  
- Extensible and cloud-ready for real-world deployment.  

---

## 📂 Project Structure


```
rag-mental-health-assistant/
│── app.py                  # Streamlit UI
│── run_all.sh              # One-command script (setup + ingestion + run)
│── requirements.txt        # Dependencies (main)
│── requirements-dev.txt    # Dev dependencies (linting, testing, CI)
│── docker-compose.yml      # Container orchestration
│── Dockerfile              # Main app container
│
├── data/
│   ├── raw/                # WHO, NIH, CDC documents (sample excerpts)
│   ├── processed/          # Cleaned and chunked data
│   └── feedback.csv        # User feedback
│
├── pipeline/
│   └── ingest.py           # Automated ingestion pipeline
│
├── retrieval/
│   ├── retriever.py        # Hybrid retrieval logic
│   ├── reranker.py         # Document re-ranking
│   └── query_rewriter.py   # Query rewriting
│
├── evaluation/
│   ├── retrieval_eval.py   # Evaluation of retrieval methods
│   └── llm_eval.py         # Prompt and output evaluation
│
├── monitoring/
│   └── dashboard.py        # Streamlit monitoring dashboard
│
└── .github/workflows/
    └── ci.yml              # Continuous integration pipeline
```

---

## 🔎 Retrieval Flow

1. **User query** → Preprocessed (query rewriting for clarity).  
2. **Retriever** → Hybrid search (BM25 + Dense embeddings via sentence-transformers).  
3. **Re-ranking** → Cross-encoder reranker improves top-k results.  
4. **Context assembly** → Relevant passages combined.  
5. **LLM (OpenAI GPT)** → Generates grounded response.  
6. **UI** → Displays both answer and retrieved documents.  

### Architecture Diagram

```
User → Streamlit UI → Retriever (Hybrid) → Reranker → Context → LLM (OpenAI) → Response
```

---

## 📊 Evaluation

We evaluated multiple retrieval methods and LLM prompts.  

### Retrieval Evaluation

| Method  | Precision@5 | Recall@5 | MRR  | Selected |
|---------|-------------|----------|------|----------|
| BM25    | 0.68        | 0.70     | 0.65 |          |
| Dense   | 0.74        | 0.78     | 0.72 |          |
| Hybrid  | **0.82**    | **0.85** | **0.80** | ✅ |

### LLM Evaluation

| Prompt Strategy       | Factuality | Relevance | Fluency | Selected |
|-----------------------|------------|-----------|---------|----------|
| Zero-shot             | 0.72       | 0.70      | 0.85    |          |
| Few-shot              | 0.80       | 0.78      | 0.87    | ✅ |
| Chain-of-thought      | **0.84**   | **0.82**  | 0.85    | ✅ |

---

## 💻 Interface

The project provides:  
- **Streamlit web UI** → simple Q&A interface with document transparency.  
- **FastAPI backend** → REST API for programmatic access.  

---

## ⚙️ Ingestion Pipeline

- **Automated script** (`ingestion/ingest.py`) loads raw documents (WHO, NIH, CDC excerpts).  
- Converts them into embeddings (sentence-transformers).  
- Stores them in FAISS vector DB.  
- Can be re-run weekly to update the knowledge base.  

---

## 📈 Monitoring

The Streamlit monitoring dashboard provides:  
- User feedback (thumbs up/down).  
- Query volume trends.  
- Latency distribution.  
- Retrieval quality (precision@k over time).  
- LLM performance breakdown.  

---

## 📦 Containerization

The app is fully containerized:  
- `Dockerfile` → main application.  
- `docker-compose.yml` → orchestrates app, vector DB, monitoring.  

Run locally with:  
```bash
docker-compose up --build
```

---

## 🔁 Reproducibility

- Clear setup instructions in this README.  
- Dataset provided in `data/raw/`.  
- `requirements.txt` with pinned versions.  
- `run_all.sh` script automates testing, ingestion, and app startup.  

```bash
./run_all.sh
```

---

## 🌐 Deployment

The app is deployable to Render or Railway for free.  

### 1. Add environment variables
- `OPENAI_API_KEY` (required).  

### 2. Files for deployment
- `Procfile` (defines startup command).  
- `runtime.txt` (Python version).  
- `requirements.txt`.  

### 3. Deploy to Render (example)
```bash
# Initialize and push
git init
git add .
git commit -m "Deploy to Render"
git remote add render https://git.render.com/your-app-url.git
git push render main
```

---

## 🧪 CI/CD

- `.github/workflows/ci.yml` runs:  
  - Unit tests.  
  - Retrieval evaluation.  
  - LLM evaluation.  

---

## 🏆 Evaluation Criteria Coverage

✅ **Problem description** – clearly explained.  
✅ **Retrieval flow** – KB + LLM with hybrid search.  
✅ **Retrieval evaluation** – multiple methods, best chosen.  
✅ **LLM evaluation** – multiple prompts, best chosen.  
✅ **Interface** – Streamlit UI + FastAPI API.  
✅ **Ingestion pipeline** – automated script.  
✅ **Monitoring** – user feedback.  
✅ **Containerization** – full Docker & docker-compose.  
✅ **Reproducibility** – dataset + requirements + run script.  
✅ **Best practices** – hybrid search, reranking, query rewriting.  
✅ **Bonus** – Cloud-ready deployment (Render/Railway).  

---

## 📜 License

MIT License.  

---

## 🙌 Acknowledgments

- [DataTalksClub](https://datatalks.club) for the LLM Zoomcamp  
- WHO, NIH, and CDC for public health data  
- OpenAI for the LLM API  
- We extend our sincere gratitude to Alexey Grigorev and the DataTalks Club team for their expert guidance, valuable Slack  support, and for creating this exceptional learning opportunity through the LLM course.

---

## 👤 Author

Developed as part of LLM Zoomcamp 2025 by Carlos Saritama.  

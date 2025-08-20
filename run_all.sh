#!/bin/bash
set -e

echo "🚀 Running full pipeline: tests → ingestion → app"

# 1. Run tests
echo "✅ Running tests..."
pytest tests/ --maxfail=1 --disable-warnings -q

# 2. Ingest data
echo "📥 Ingesting data into the knowledge base..."
python pipelines/ingest.py

# 3. Start the Streamlit app
echo "🌐 Starting the Streamlit UI..."
streamlit run app/streamlit_app.py --server.port=8501

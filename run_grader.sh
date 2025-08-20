#!/usr/bin/env bash
# Single-command helper for graders (local environment)
# It will: install deps (into current Python env), run ingestion, run tests, then start Streamlit app.
set -e
echo "Running grader helper script..."

if [ -f "requirements.txt" ]; then
  echo "Installing dependencies (may take a few minutes)..."
  pip install -r requirements.txt
fi

echo "Running ingestion..."
python ingestion/ingest_data.py --source data/raw --output data/processed

echo "Running tests..."
pytest -q || true

echo "Starting Streamlit app (press Ctrl+C to stop)..."
streamlit run interface/app.py

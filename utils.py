"""Utility helpers used across the project."""

import os, json
from monitoring.feedback_store import save_feedback as _save_feedback

def load_documents(folder="data/processed"):
    path = os.path.join(folder, "chunks.json")
    if not os.path.exists(path):
        return []
    return json.load(open(path, "r", encoding="utf-8"))

def save_feedback(query, response, feedback, rating=None, source_snippet=None):
    # Wrapper to store feedback with optional rating and source snippet
    _save_feedback(query, response, feedback, rating=rating, source_snippet=source_snippet)

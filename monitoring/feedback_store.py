#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""Feedback persistence helpers (stores CSV columns: query,response,feedback,ts,rating,source_snippet)"""
import csv, os
from datetime import datetime

FEEDBACK_CSV = "monitoring/user_feedback.csv"

def save_feedback(query, response, feedback, rating=None, source_snippet=None):
    os.makedirs(os.path.dirname(FEEDBACK_CSV), exist_ok=True)
    ts = datetime.utcnow().isoformat()
    # Ensure rating and source_snippet are optional
    row = [query, response, feedback, ts, rating if rating is not None else '', source_snippet if source_snippet is not None else '']
    with open(FEEDBACK_CSV, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

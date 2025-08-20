#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 


"""Basic query rewriting utilities:
- normalize_query: simple lowercasing and punctuation removal
- expand_query: add synonyms/alternate phrases for broader retrieval (simple rule-based)
"""
import re

SYNONYMS = {
    "depression": ["depressive disorder", "low mood"],
    "anxiety": ["anxiety disorder", "worry"],
    "panic": ["panic attack"]
}

def normalize_query(q: str) -> str:
    q = q.lower()
    q = re.sub(r"[^a-z0-9\s]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()
    return q

def expand_query(q: str) -> str:
    qn = normalize_query(q)
    parts = qn.split()
    extras = []
    for p in parts:
        extras += SYNONYMS.get(p, [])
    if extras:
        return qn + " " + " ".join(extras)
    return qn

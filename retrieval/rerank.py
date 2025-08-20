#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 


"""
Reranking module: simple lexical overlap heuristic.
"""

def rerank_by_overlap(candidates, query):
    qset = set(query.lower().split())
    scored = []
    for c in candidates:
        text = c.get("text", "") if isinstance(c, dict) else c
        words = set(text.lower().split())
        overlap = len(qset & words)
        scored.append((overlap, c))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [c for _, c in scored]

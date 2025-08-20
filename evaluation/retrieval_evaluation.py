#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""Retrieval evaluation: compare Simple, Vector, and Hybrid retrieval strategies.
Computes recall@k, precision@k and MRR on a small labeled dataset.
"""

import json
import math
from retrieval.retriever import SimpleRetriever, HybridRetriever
from retrieval.vector_store import build_index, search as vector_search
from utils import load_documents

# Example labeled queries with ground-truth snippets (for demo)
EVAL_QUERIES = [
    {"q": "signs of depression", "gt": ["depression is common"]},
    {"q": "manage anxiety breathing", "gt": ["breathing exercises", "manage anxiety"]},
    {"q": "support a friend with depression", "gt": ["support", "seek professional help"]}
]

def precision_at_k(results, ground_truth, k=3):
    if not results:
        return 0.0
    retrieved_texts = [r.get("text","") for r in results[:k]]
    relevant = sum(1 for t in retrieved_texts for gt in ground_truth if gt in t)
    return relevant / min(k, len(retrieved_texts))

def recall_at_k(results, ground_truth, k=3):
    if not ground_truth:
        return 0.0
    retrieved_texts = [r.get("text","") for r in results[:k]]
    hits = sum(1 for gt in ground_truth if any(gt in t for t in retrieved_texts))
    return hits / len(ground_truth)

def mrr(results, ground_truth):
    # Mean Reciprocal Rank for single query
    for rank, r in enumerate(results, start=1):
        for gt in ground_truth:
            if gt in r.get("text",""):
                return 1.0 / rank
    return 0.0

def evaluate(chunks):
    # Ensure vector index built for vector/hybrid
    build_index(chunks)
    simple = SimpleRetriever(chunks)
    hybrid = HybridRetriever(chunks)

    metrics = {"simple": [], "vector": [], "hybrid": []}
    for item in EVAL_QUERIES:
        q = item["q"]
        gt = item["gt"]

        # Simple retrieval
        s_res = simple.search(q, k=5)
        # Vector retrieval
        v_res = vector_search(q, top_k=5)
        # Hybrid retrieval
        h_res = hybrid.search(q, k=5)

        for name, res in [("simple", s_res), ("vector", v_res), ("hybrid", h_res)]:
            p = precision_at_k(res, gt, k=3)
            r = recall_at_k(res, gt, k=3)
            mm = mrr(res, gt)
            metrics[name].append({"query": q, "precision@3": p, "recall@3": r, "mrr": mm})

    return metrics

def print_metrics(metrics):
    for name, vals in metrics.items():
        print(f"\n=== {name.upper()} ===")
        avg_precision = sum(v["precision@3"] for v in vals)/len(vals)
        avg_recall = sum(v["recall@3"] for v in vals)/len(vals)
        avg_mrr = sum(v["mrr"] for v in vals)/len(vals)
        print(f"Avg precision@3: {avg_precision:.3f}")
        print(f"Avg recall@3: {avg_recall:.3f}")
        print(f"Avg MRR: {avg_mrr:.3f}")
        for v in vals:
            print(v)

if __name__ == '__main__':
    chunks = json.load(open('data/processed/chunks.json'))
    metrics = evaluate(chunks)
    print_metrics(metrics)

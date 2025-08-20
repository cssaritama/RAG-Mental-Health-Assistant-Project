#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 


"""Retrieval strategies with query rewriting integration."""
from typing import List
from retrieval.vector_store import search as vector_search
from retrieval.rerank import rerank_by_overlap
from retrieval import query_rewrite

class SimpleRetriever:
    def __init__(self, chunks: List[dict]):
        self.chunks = chunks

    def search(self, query: str, k: int = 3):
        q = query.lower()
        matches = [c for c in self.chunks if q in c['text'].lower()]
        return matches[:k]

class HybridRetriever:
    def __init__(self, chunks: List[dict]):
        self.chunks = chunks

    def search(self, query: str, k: int = 3):
        # rewrite and expand query
        expanded = query_rewrite.expand_query(query)
        candidates = vector_search(expanded, top_k=10)
        # simple rerank by overlap with original query
        reranked = rerank_by_overlap(candidates, query)
        return reranked[:k]

#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""
LLM evaluation helpers.
- run_prompt_comparison: runs multiple prompts and collects outputs
- simple_metrics: counts keyword hits and returns length-based metrics
"""

from llm.query_llm import query_openai

def run_prompt_comparison(question, context_chunks, prompt_fns):
    results = {}
    for name, fn in prompt_fns.items():
        prompt = fn(question, context_chunks)
        out = query_openai(prompt)
        results[name] = out
    return results

def simple_metrics(output, expected_keywords=None):
    expected_keywords = expected_keywords or []
    hits = sum(1 for kw in expected_keywords if kw.lower() in output.lower())
    return {"keyword_hits": hits, "length": len(output.split())}

#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""LLM evaluation: compare multiple prompt templates and settings.
This script runs prompt variants and computes simple keyword-based metrics and (optionally) embedding similarity.
"""
from llm.evaluation import run_prompt_comparison, simple_metrics
from llm.prompt_templates import compose_prompt
from llm.query_llm import query_openai

def main():
    question = "How can I support a friend with depression?"
    chunks = [{"text":"Depression is common and treatable."}]

    prompts = {
        "baseline": compose_prompt,
        "with_resources": lambda q,c: compose_prompt(q,c) + "\nPlease include at least two community resources.",
        "safety_first": lambda q,c: compose_prompt(q,c) + "\nInclude safety recommendations and encourage seeking professional help."
    }

    results = run_prompt_comparison(question, chunks, prompts)
    for name, out in results.items():
        metrics = simple_metrics(out, expected_keywords=["depression","support","professional"])
        print(f"Prompt: {name}\nOutput: {out}\nMetrics: {metrics}\n---\n")

if __name__ == '__main__':
    main()

#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""
Prompt templates for the assistant. Keep prompts safe and non-diagnostic.
"""

def compose_prompt(question: str, context_chunks):
    context_text = "\n\n---\n\n".join([c["text"] for c in context_chunks])
    prompt = f"""You are a helpful, evidence-based assistant that provides non-diagnostic mental health information.
Use the provided context excerpts to answer the user's question concisely and include a short 'Sources' section indicating the most relevant context excerpts.

Context:
{context_text}

Question: {question}

Answer:""""
    return prompt

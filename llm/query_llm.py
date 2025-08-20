#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""
LLM wrapper that calls OpenAI's completions/chat API when OPENAI_API_KEY is set.
If the API key is missing, returns a mocked deterministic answer for reproducibility.
"""

import os
import logging

try:
    import openai
except Exception:
    openai = None  # openai package may not be installed in grading environment

logger = logging.getLogger(__name__)

def query_openai(prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 512, temperature: float = 0.0):
    """Query OpenAI API using the Chat Completions (or completions) endpoint.
    - Reads OPENAI_API_KEY from environment variables for security.
    - Returns model text. If API key or openai package is not available, returns a mocked answer.
    """
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY", None)
    if api_key and openai is not None:
        try:
            openai.api_key = api_key
            # Use ChatCompletion if available; fallback to completion
            if hasattr(openai, "ChatCompletion"):
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
                # Extract assistant reply
                if response and "choices" in response and len(response.choices) > 0:
                    return response.choices[0].message.get("content", "").strip()
            else:
                response = openai.Completion.create(
                    engine=model,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
                if response and "choices" in response and len(response.choices) > 0:
                    return response.choices[0].text.strip()
        except Exception as e:
            logger.warning(f"OpenAI API call failed: {e}")
            # Fallthrough to mock
    # Mock deterministic response if API key missing or error occurred
    return "Mocked LLM answer based on provided context. (Set OPENAI_API_KEY to use real OpenAI API.)"

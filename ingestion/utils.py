#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""

Ingestion utilities.
All comments and docstrings are in English.

"""




def clean_text(text: str) -> str:
    """Normalize whitespace and remove excessive newlines."""
    return " ".join(text.replace("\r", "\n").split())

def chunk_text(text: str, chunk_size: int = 200, overlap: int = 50):
    """Split text into word-based chunks with specified overlap."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        start = max(end - overlap, end)
    return chunks

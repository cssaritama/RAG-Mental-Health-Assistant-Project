#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""
Automated ingestion script:
- Loads text files from --source
- Cleans and chunks texts
- Writes chunks to --output/chunks.json
"""

import argparse
from pathlib import Path
import json
from ingestion.utils import clean_text, chunk_text

def load_texts(source_folder: str):
    p = Path(source_folder)
    texts = []
    for f in sorted(p.glob("*.txt")):
        texts.append({"source": f.name, "text": f.read_text(encoding="utf-8")})
    return texts

def main(source: str, output: str):
    texts = load_texts(source)
    chunks = []
    for doc in texts:
        cleaned = clean_text(doc["text"])
        for i, ch in enumerate(chunk_text(cleaned, chunk_size=200, overlap=50)):
            chunks.append({"source": doc["source"], "chunk_id": i, "text": ch})
    outp = Path(output)
    outp.mkdir(parents=True, exist_ok=True)
    outp.joinpath("chunks.json").write_text(json.dumps(chunks, indent=2, ensure_ascii=False))
    print(f"Ingested {len(chunks)} chunks and wrote to {outp / 'chunks.json'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/raw", help="Source folder with raw text files")
    parser.add_argument("--output", default="data/processed", help="Output folder for chunks.json")
    args = parser.parse_args()
    main(args.source, args.output)

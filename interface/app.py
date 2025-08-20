#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""
Streamlit UI enhanced:
- select retrieval method (simple, vector, hybrid)
- shows which method was used
- displays evaluation summaries by importing evaluation scripts
"""

import streamlit as st
import json, io, sys
from utils import load_documents, save_feedback
from retrieval.retriever import SimpleRetriever, HybridRetriever
from retrieval.vector_store import build_index, search as vector_search
from retrieval.rerank import rerank_by_overlap
from llm.prompt_templates import compose_prompt
from llm.query_llm import query_openai
import evaluation.retrieval_evaluation as re_eval
import evaluation.llm_evaluation as llm_eval

st.set_page_config(page_title='Mental Health RAG Assistant', layout='wide')
st.title('🧠 Mental Health RAG Assistant (Enhanced)')

# Load chunks
chunks = []
try:
    chunks = load_documents('data/processed')
except Exception:
    try:
        with open('data/processed/chunks.json','r',encoding='utf-8') as f:
            chunks = json.load(f)
    except Exception:
        chunks = []

if not chunks:
    st.warning('No processed data found. Run ingestion first (ingestion/ingest_data.py).')

# Retrieval method selection
method = st.sidebar.selectbox('Retrieval method', ['hybrid','vector','simple'], index=0)
st.sidebar.markdown('Select retrieval method to use for the next query.')

# Query input
query = st.text_input('Ask a question:')
if query:
    st.write('Selected retrieval method:', method.upper())
    build_index(chunks)
    if method == 'simple':
        r = SimpleRetriever(chunks)
        results = r.search(query, k=5)
    elif method == 'vector':
        results = vector_search(query, top_k=5)
    else:
        r = HybridRetriever(chunks)
        results = r.search(query, k=5)

    # Attempt reranking for better ordering (if candidates are dicts)
    try:
        reranked = rerank_by_overlap(results, query)
    except Exception:
        reranked = results

    # Build prompt from top-3
    prompt = compose_prompt(query, reranked[:3] if reranked else [])
    answer = query_openai(prompt)

    st.subheader('Answer')
    st.write(answer)

    st.subheader('Top source snippets')
    for i, c in enumerate(reranked[:5]):
        st.write(f"{i+1}. {c.get('text', c)[:350]}")

    rating = st.sidebar.slider('Rate this answer (1-5)', 1, 5, 4)
    if st.button('Submit feedback'):
        save_feedback(query, answer, 'Yes' if rating >=4 else 'No', rating=rating, source_snippet=(reranked[0].get('text')[:200] if reranked else ''))
        st.success('Feedback saved!')

# Evaluation summary section
st.sidebar.markdown('---')
if st.sidebar.button('Show evaluation summary'):
    # Capture stdout from evaluation scripts
    buf = io.StringIO()
    orig_stdout = sys.stdout
    try:
        sys.stdout = buf
        # run retrieval evaluation (prints metrics)
        try:
            re_eval_main = getattr(re_eval, 'evaluate', None)
            if callable(re_eval_main):
                metrics = re_eval_main(load_documents('data/processed'))
                # pretty print metrics
                import pprint
                pprint.pprint(metrics)
            else:
                # fallback to running as script
                import runpy
                runpy.run_module('evaluation.retrieval_evaluation', run_name='__main__')
        except Exception as e:
            print('Retrieval evaluation failed:', e)
        # run llm evaluation
        try:
            import runpy
            runpy.run_module('evaluation.llm_evaluation', run_name='__main__')
        except Exception as e:
            print('LLM evaluation failed:', e)
    finally:
        sys.stdout = orig_stdout
    st.subheader('Evaluation Summary (logs)')
    st.text(buf.getvalue())

#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 


from retrieval.retriever import SimpleRetriever
def test_simple_retriever():
    chunks = [{"text":"Depression is common."}, {"text":"Anxiety is manageable."}]
    r = SimpleRetriever(chunks)
    out = r.search("depression")
    assert len(out) >= 0


#**Author:** Carlos Stalin Saritama Atopo  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 


from llm.query_llm import query_openai
def test_llm_mock():
    out = query_openai("Test")
    assert "Mocked LLM answer" in out

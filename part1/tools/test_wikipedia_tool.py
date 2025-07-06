from tools.wikipedia_tool import run_wikipedia_search

def test_basic_query():
    query = "Alan Turing"
    result = run_wikipedia_search(query)
    assert "Alan Turing" in result or "mathematician" in result

def test_disambiguation():
    query = "Mercury"
    result = run_wikipedia_search(query)
    assert "Did you mean one of these?" in result or "Wikipedia Summary" in result

def test_no_result():
    query = "asdlkjfasdlfkjasdf"  # gibberish
    result = run_wikipedia_search(query)
    assert "No Wikipedia page found" in result or "No relevant results found" in result

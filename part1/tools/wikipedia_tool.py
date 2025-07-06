import wikipedia

def run_wikipedia_search(query: str) -> str:
    """
    Perform a Wikipedia search and return a summary of the most relevant result.

    Args:
        query (str): The user query string.

    Returns:
        str: A summary of the top Wikipedia result or an error message.
    """
    try:
        search_results = wikipedia.search(query)
        if not search_results:
            return "No relevant results found on Wikipedia."

        page_title = search_results[0]
        summary = wikipedia.summary(page_title, sentences=3)
        return f"Wikipedia Summary for '{page_title}':\n{summary}"
    
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is too ambiguous. Did you mean one of these?\n{e.options[:5]}"
    
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found matching your query."

    except Exception as e:
        return f"An error occurred while searching Wikipedia: {str(e)}"

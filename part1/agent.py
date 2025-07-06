from tools.llama_tool import run_llama
from tools.wikipedia_tool import run_wikipedia_search
from prompts import SYSTEM_PROMPT

def run_agent(user_prompt: str) -> str:
    """
    Routes the user prompt to either the Wikipedia tool (for search queries)
    or the LLaMA model (for reasoning/completion).

    Args:
        user_prompt (str): The input query from the user.

    Returns:
        str: The generated response from either the tool or LLaMA.
    """
    if "search" in user_prompt.lower() or "find" in user_prompt.lower():
        return run_wikipedia_search(user_prompt)
    else:
        prompt = SYSTEM_PROMPT.format(user_input=user_prompt)
        return run_llama(prompt)

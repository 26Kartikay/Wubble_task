from tools.openai_tool import use_openai
from tools.wiki_tool import use_wikipedia
from prompts import SYSTEM_PROMPT

def run_agent(user_prompt: str) -> str:
    # Simple routing logic based on keywords
    if "define" in user_prompt.lower():
        return use_wikipedia(user_prompt)
    else:
        return use_openai(SYSTEM_PROMPT.format(user_input=user_prompt))

import json
from agent import run_agent

# Define a list of test prompts with expected keywords or phrases
TEST_CASES = [
    {
        "id": "basic-info",
        "prompt": "What is Artificial Intelligence?",
        "expected_keywords": ["intelligence", "machines", "simulate", "human"],
    },
    {
        "id": "edge-case-empty",
        "prompt": "",
        "expected_keywords": ["error", "invalid", "empty"],
    },
    {
        "id": "search-related",
        "prompt": "Search for the latest news on climate change",
        "expected_keywords": ["climate", "change", "news"],
    },
    {
        "id": "off-topic",
        "prompt": "Tell me a joke about databases",
        "expected_keywords": ["joke", "data", "sql", "funny"],
    },
    {
        "id": "define-concept",
        "prompt": "Define the term overfitting in machine learning",
        "expected_keywords": ["overfitting", "model", "training", "data"],
    },
]

def evaluate_response(prompt, response, expected_keywords):
    """Simple keyword-based heuristic evaluation."""
    if not response or not isinstance(response, str):
        return "FAIL", "Empty or invalid response"

    match_count = sum(1 for keyword in expected_keywords if keyword.lower() in response.lower())
    pass_threshold = int(0.5 * len(expected_keywords))

    if match_count >= pass_threshold:
        return "PASS", f"{match_count}/{len(expected_keywords)} keywords matched"
    else:
        return "FAIL", f"Only {match_count}/{len(expected_keywords)} keywords matched"

def run_all_evaluations():
    results = []
    for case in TEST_CASES:
        response = run_agent(case["prompt"])
        status, reason = evaluate_response(case["prompt"], response, case["expected_keywords"])
        results.append({
            "id": case["id"],
            "prompt": case["prompt"],
            "response": response,
            "status": status,
            "reason": reason
        })

    return results

if __name__ == "__main__":
    final_results = run_all_evaluations()
    print(json.dumps(final_results, indent=2))

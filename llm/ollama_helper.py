import subprocess
from functools import lru_cache

@lru_cache(maxsize=100)
def explain_decision(user_input, model_output):
    prompt = f"""
You are a banking AI assistant.

Customer details:
{user_input}

Model decision:
{model_output}

Explain the decision in simple banking language.
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout
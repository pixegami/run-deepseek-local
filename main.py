import ollama
from util import remove_think_tags


MODEL = "deepseek-r1:7b"
PROMPT = "Hello! Tell me about yourself."


# Generate it in one shot.
result = ollama.generate(model=MODEL, prompt=PROMPT)
response = result["response"]
print("✨ Raw Response", response)

cleaned_response = remove_think_tags(response)
print("✅ Cleaned Response", cleaned_response)

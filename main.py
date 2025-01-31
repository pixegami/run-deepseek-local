import ollama

MODEL = "deepseek-r1:7b"
PROMPT = "Hello! Tell me about yourself."

# Generate it in one shot.
result = ollama.generate(model=MODEL, prompt=PROMPT)
response = result["response"]
print("✨ Raw Response", response)

# Run Deepseek R1 Locally

Here's some ways to quickly get started running [Deepseek R1](https://www.deepseek.com/) locally on your machine. I ran these using an M1 Macbook Pro, using the 4.7GB [deepseek-r1:7b](https://ollama.com/library/deepseek-r1:7b) model

## Run Deepseek with LM Studio (UI)

LM Studio is a free app that lets you run language models on your own machine. 

* Download it from https://lmstudio.ai.
* Download the Deepseek R1 (Qwen) model through LM Studio's interface and start chatting. The interface displays token usage and shows the model's thought process as it generates responses.

I used the 7B parameter model, which is OK for testing functionality, but not really that powerful.

## Run with Ollama (in Terminal)

Ollama is a free and open-source tool that allows you to run large language models (LLMs) directly on your local machine. You can run it via a chat interface in your terminal, or serve it as a REST API on localhost.

1. Download and install Ollama:
    - Visit https://ollama.com/ and download the appropriate version for your operating system.
    - Run the installer and follow the on-screen instructions.

2. Verify Ollama installation by checking the version:

```sh
ollama --version
```

3. Start the Ollama server:

```sh
ollama serve
```

4. Open a new terminal window.

5. Download and run the DeepSeek-R1 model (could take a few minutes):

```sh
ollama run deepseek-r1:7b
```

6. Once the download is complete, you can start interacting with DeepSeek-R1 in your terminal by typing your prompts and pressing `Enter`.


## Run via Python (via Ollama)

If you want to use it as part of your Python application, you can run it by calling the local server directly (via REST), but it's easier to use the `ollama` library.

```sh
# Make sure the Ollama server is running.
ollama serve
```

```sh
# Install Ollama Python library
pip install ollama
```

Run a query via Python (see `main,py`):

```python
import ollama

MODEL = "deepseek-r1:7b"
PROMPT = "Hello! What is the capital of France?"

# Generate it in one shot.
result = ollama.generate(model=MODEL, prompt=PROMPT)
response = result["response"]
print("✨ Raw Response", response)
```

### Thinking Tags

If the query is "complex", the raw response will have `<think>...</think>` tags to show the thought process. For example, for the query:

```text
Hello! Tell me about yourself.
```

The response is:

```text
<think>
I'm DeepSeek-R1, an AI assistant created exclusively by the Chinese Company DeepSeek. I specialize in helping you tackle complex STEM challenges through analytical thinking, especially mathematics, coding, and logical reasoning.
</think>

Hello! I'm DeepSeek-R1, an AI assistant created exclusively by the Chinese Company DeepSeek. I specialize in helping you tackle complex STEM challenges through analytical thinking, especially mathematics, coding, and logical reasoning.
```

This is useful to read, but can sometimes get in the way. So we have a function in the `util.py` file to clean it up.

```python
from util import remove_think_tags

cleaned_response = remove_think_tags(response)
print("✅ Cleaned Response", cleaned_response)
```

### Streaming

If you want to stream the response instead of getting it all in one go, you can use the `stream` argument, and then iterate through the response.

```python
# Generate it in a stream.
for chunk in ollama.generate(model=MODEL, prompt=PROMPT, stream=True):
    print(chunk["response"], end="", flush=True)
```
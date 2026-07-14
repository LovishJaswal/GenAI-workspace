# Install the required package:
# uv add requests

# Requirements:
# - Ollama installed and running locally.
# - llama3.2:1b model downloaded.
#
# Start Ollama:
# ollama serve

import requests

# Send a chat request to the local Ollama server
response = requests.post(
    url="http://localhost:11434/api/chat",
    json={
        "model": "llama3.2:1b",
        "messages": [
            {
                "role": "user",
                "content": "Why is the sky blue?",
            }
        ],
        "stream": False,
    },
)

response.raise_for_status()

# Print the model's response
print(response.text)
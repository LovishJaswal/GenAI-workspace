# Install the required package:
# uv add requests

import requests

from config import GEMINI_API_KEY


# Gemini REST API endpoint
URL = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models/gemini-2.5-flash:generateContent"
)

# Request headers
headers = {
    "Content-Type": "application/json",
}

# API key
params = {
    "key": GEMINI_API_KEY,
}

# Request body
data = {
    "contents": [
        {
            "parts": [
                {"text": "Explain API keys"},
            ],
        }
    ]
}

# Send the request
response = requests.post(URL, headers=headers, params=params, json=data)

# Extract and print the generated text
result = response.json()
print(result["candidates"][0]["content"]["parts"][0]["text"])
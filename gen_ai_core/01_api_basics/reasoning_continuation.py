# Install the required package:
# uv add requests

# Required:
# OPEN_ROUTER_API_KEY
# (Stored in .env and loaded through config.py)

# Purpose:
# Demonstrates reasoning continuation by sending the model's
# reasoning_details back in a follow-up request.

import json
import requests

from config import OPEN_ROUTER_API_KEY

URL = "https://openrouter.ai/api/v1/chat/completions"

# First request
response = requests.post(
    url=URL,
    headers={
        "Authorization": f"Bearer {OPEN_ROUTER_API_KEY}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "nex-agi/nex-n2-pro:free",
        "messages": [
            {
                "role": "user",
                "content": "How many r's are in the word 'strawberry'?"
            }
        ],
        # Enable reasoning if required
        # "reasoning": {"enabled": True}
    }),
)

response.raise_for_status()

# Extract the assistant response
response = response.json()["choices"][0]["message"]

# Preserve the reasoning details for the next request
messages = [
    {
        "role": "user",
        "content": "How many r's are in the word 'strawberry'?"
    },
    {
        "role": "assistant",
        "content": response.get("content"),
        "reasoning_details": response.get("reasoning_details"),
    },
    {
        "role": "user",
        "content": "Are you sure? Think carefully."
    },
]

# Second request - continue reasoning
response2 = requests.post(
    url=URL,
    headers={
        "Authorization": f"Bearer {OPEN_ROUTER_API_KEY}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "nex-agi/nex-n2-pro:free",
        "messages": messages,
        "reasoning": {"enabled": True},
    }),
)

response2.raise_for_status()

print(response2.json()["choices"][0]["message"]["content"])
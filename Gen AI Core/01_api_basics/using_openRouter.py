# Install the SDK:
# uv add openai

from openai import OpenAI

from config import OPEN_ROUTER_API_KEY, OPEN_ROUTER_BASE_URL


# Create an OpenAI client configured for OpenRouter
client = OpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url=OPEN_ROUTER_BASE_URL,
)

# Send a chat completion request
response = client.chat.completions.create(
    model="google/gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Explain APIs"},
    ],
    max_tokens=500,
)

# Print the model's response
print(response.choices[0].message.content)
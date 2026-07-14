# Install the SDK:
# uv add openai

from openai import OpenAI

from config import GEMINI_API_KEY, GEMINI_BASE_URL


# Create an OpenAI client configured for Gemini
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL,
)

# Send a chat completion request
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a teacher teaching kids"},
        {"role": "user", "content": "Explain API keys"},
    ],
)

# Print the model's response
print(response.choices[0].message.content)
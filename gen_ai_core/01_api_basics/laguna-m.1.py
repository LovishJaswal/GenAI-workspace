# Install the SDK:
# uv add openai

from openai import OpenAI

from config import OPEN_ROUTER_API_KEY, OPEN_ROUTER_BASE_URL


# Create an OpenAI client configured for OpenRouter
client = OpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url=OPEN_ROUTER_BASE_URL,
)

# Send a request using the Responses API
response = client.responses.create(
    model="poolside/laguna-m.1:free",
    instructions="You are a teacher teaching kids",
    input="Explain API keys",
)

# Print the model's response
print(response.output_text)
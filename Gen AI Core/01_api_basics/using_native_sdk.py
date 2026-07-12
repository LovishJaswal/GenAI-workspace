# Install the SDK:
# uv add google-genai

from google import genai

from config import GEMINI_API_KEY


# Create a Gemini client using the API key from .env
client = genai.Client(api_key=GEMINI_API_KEY)

# Send a prompt to the Gemini model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain API keys",
)

# Print the model's response
print(response.text)
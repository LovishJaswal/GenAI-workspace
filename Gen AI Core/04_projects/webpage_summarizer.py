# Install the required packages:
# uv add requests bs4 fake-useragent openai

# Required:
# OPEN_ROUTER_API_KEY
# OPEN_ROUTER_BASE_URL
# (Stored in .env and loaded through config.py)

# Output:
# Creates summarized.txt containing the webpage summary.

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from openai import OpenAI

from config import OPEN_ROUTER_API_KEY, OPEN_ROUTER_BASE_URL


# Get the webpage URL from the user
url = input("Enter the webpage URL: ")

# Create a browser-like User-Agent
agent = UserAgent()

# Fetch the webpage
try:
    response = requests.get(
        url,
        headers={"User-Agent": agent.chrome},
        timeout=10,
    )
    response.raise_for_status()

except Exception as e:
    print("Failed to fetch webpage:", e)
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Remove unnecessary HTML tags
for tag in soup(["nav", "footer", "script", "style", "header", "aside"]):
    tag.decompose()

# Extract the main content
content = soup.find(id="main")
if content is None:
    content = soup.body

# Convert HTML to plain text
raw_text = content.get_text(separator="\n")

# Remove empty lines
lines = [line.strip() for line in raw_text.split("\n") if line.strip()]

# Remove consecutive duplicate lines
clean_lines = []
for line in lines:
    if not clean_lines or clean_lines[-1] != line:
        clean_lines.append(line)

clean_text = "\n".join(clean_lines)

# Create an OpenAI client configured for OpenRouter
try:
    client = OpenAI(
        api_key=OPEN_ROUTER_API_KEY,
        base_url=OPEN_ROUTER_BASE_URL,
    )

    response = client.responses.create(
        model="poolside/laguna-m.1:free",
        instructions="Summarize the following webpage",
        input=clean_text,
    )

except Exception as e:
    print("Failed to communicate with the model:", e)
    exit()

# Extract the generated summary
answer = response.output_text

# Save the summary to a text file
with open("summarized.txt", "w", encoding="utf-8") as file:
    file.write(answer)

print("Response saved successfully!")
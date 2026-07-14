# Install the required packages:
# uv add requests bs4 html5lib

# Output:
# Creates file.txt containing the cleaned webpage text.
# This file will be used in later examples (e.g., parsing, chunking, summarization).

import requests
from bs4 import BeautifulSoup

# HTML parser to use:
# - "html.parser" (fast, built into Python)
# - "html5lib" (slower, more accurate for malformed HTML)
PARSER = "html.parser"

# Send a GET request to the webpage
response = requests.get("https://www.w3schools.com/python/python_virtualenv.asp")
response.raise_for_status()  # Raise an exception if the request fails

# Parse the HTML content
soup = BeautifulSoup(response.text, PARSER)

# Remove unnecessary HTML tags
for tag in soup(["nav", "footer", "script", "style", "header", "aside"]):
    tag.decompose()

# Try to extract the main content of the page
content = soup.find(id="main")

# Fallback to the entire body if the main section isn't found
if content is None:
    content = soup.body

# Extract plain text from the HTML
raw_text = content.get_text(separator="\n")

# Remove empty lines and strip whitespace
lines = [line.strip() for line in raw_text.split("\n") if line.strip()]

# Remove consecutive duplicate lines
clean_lines = []
for line in lines:
    if not clean_lines or clean_lines[-1] != line:
        clean_lines.append(line)

# Join the cleaned lines into a single string
clean_text = "\n".join(clean_lines)

# Save the cleaned text to a file
with open("file.txt", "w", encoding="utf-8") as file:
    file.write(clean_text)

print(f"Saved {len(clean_lines)} clean lines to file.txt")
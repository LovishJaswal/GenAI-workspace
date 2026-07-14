# Install the required packages:
# uv add requests bs4 fake-useragent

# Purpose:
# Demonstrates how to send a request using a browser-like User-Agent.
# Some websites block requests that don't include a valid User-Agent.

import requests
from fake_useragent import UserAgent

# Create a browser-like User-Agent
agent = UserAgent()

# Uncomment to see the available User-Agent methods
# print(agent.__dict__)

# Fetch the webpage using a Chrome User-Agent
response = requests.get(
    "https://www.geeksforgeeks.org/python/python-data-types/",
    headers={"User-Agent": agent.chrome},
)

response.raise_for_status()

# Print the raw HTML of the webpage
print(response.text)
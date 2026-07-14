# Install the required package:
# uv add bs4

# Required file:
# html_tags_and_attributes.txt
# (Place this file in the same directory as this script.)

from bs4 import BeautifulSoup

# Read the local HTML file
with open("html_tags_and_attributes.txt", "r", encoding="utf-8") as file:
    data = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(data, "html.parser")

    # Print the formatted HTML
    # print(soup.prettify())

# Access HTML elements
# print(soup.head.title.text)
# print(soup.head.meta)

# Find HTML tags
# print(soup.find_all("div"))
# print(soup.find("div"))

# Search elements by id or class
# print(soup.find(id="..."))
# print(soup.find(class_="..."))

# Find all links inside the navigation bar
# print(soup.body.header.nav.find_all("a"))

# Alternative way to access the navigation bar
# print(soup.find("nav").find_all("a"))

# Doesn't work because HTML attributes are accessed using dictionary syntax
# print(soup.body.header.nav.a.href)

# Print the href attribute of the first <a> tag
print(soup.a["href"])

# Good web scraping practices:
# - Add intentional delays between requests.
# - Avoid sending too many requests to the same website.
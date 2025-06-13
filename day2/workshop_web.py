import requests
from bs4 import BeautifulSoup

# Get content from website
url = "https://en.wikipedia.org/wiki/Thailand"
response = requests.get(url)
print(response.status_code)
content = response.content

# Read content from html
soup = BeautifulSoup(content, 'html.parser')

# parse from first paragraph
selector = "#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(12)"

element = soup.select_one(selector)
print(element.get_text())
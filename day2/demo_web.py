import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Thailand"
response = requests.get(url)

bs = BeautifulSoup(response.content, "html.parser")
xpath = '#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(12)'
element = bs.select_one(xpath)
if element:
    print(element.get_text())
else:
    print(f"No element found for xpath: {xpath}")
import requests
from bs4 import BeautifulSoup

url = 'https://github.com/ivvve?tab=repositories'

req = requests.get(url)
html = req.text
html = BeautifulSoup(html, 'html.parser')

# print(html.prettify())

repo_titles = html.select('#user-repositories-list h3 a')
data = {}

for title in repo_titles:
    title_text = title.text.replace('\n', '').strip()
    href = title.get('href')
    data[title_text] = href

print(data)


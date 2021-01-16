import requests

from bs4 import BeautifulSoup

word = input().strip()
url = input().strip()

tree = BeautifulSoup(requests.get(url).content, 'html.parser')

paragraphs = tree.find_all('p')

for p in paragraphs:
    if word in p.text:
        print(p.text)
        break

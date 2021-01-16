import requests

from bs4 import BeautifulSoup

url = input().strip()

tree = BeautifulSoup(requests.get(url).content, 'html.parser')

heading = tree.find('h1')

print(heading.text)

import requests

from bs4 import BeautifulSoup

index = int(input().strip())
url = input().strip()

tree = BeautifulSoup(requests.get(url).content, 'html.parser')

subtitles = tree.find_all('h2')

print(subtitles[index].text)

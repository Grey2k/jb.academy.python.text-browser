import requests

from bs4 import BeautifulSoup

act_num = int(input().strip())
url = input().strip()

tree = BeautifulSoup(requests.get(url).content, 'html.parser')

links = tree.find_all('a')

print(links[act_num - 1].get('href'))

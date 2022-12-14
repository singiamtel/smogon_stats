import requests
from bs4 import BeautifulSoup

url = 'https://www.smogon.com/stats/'
tiers = ['gen8anythinggoes-0', 'gen8anythinggoes-1500', 'gen8anythinggoes-1630', 'gen8anythinggoes-1760']

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

urls = []
ignore = ["./", "../"]
for a in soup.find_all('a'):
    if a.get("href") in ignore:
        continue
    for tier in tiers:
        urls.append(url + a.get("href") + "chaos/" + tier + ".json")

with open("urls.txt", "w") as f:
    for url in urls:
        f.write(f'{url}\n')

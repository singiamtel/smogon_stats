import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.smogon.com/stats/'
tiers = ['gen7anythinggoes-0', 'gen7anythinggoes-1500', 'gen7anythinggoes-1630', 'gen7anythinggoes-1760']

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

urls = []
ignore = ["./", "../"]
for a in soup.find_all('a'):
    if a.get("href") in ignore:
        continue
    for tier in tiers:
        # urls.append([a.get("href")[:-1] + "-" + tier, url + a.get("href") + "chaos/" + tier + ".json"])
        urls.append(url + a.get("href") + "chaos/" + tier + ".json")

with open("urls.txt", "w") as f:
    for url in urls:
        # f.write(f'{url[0]} {url[1]}\n')
        f.write(f'{url}\n')

# print("Fetched urls correctly, now fetching data")
# for url in urls:
#     print("Fetching data from: " + url[0])
#     with open(url[0], "w") as f:
#         response = requests.get(url[1])
#         f.write(url[1])

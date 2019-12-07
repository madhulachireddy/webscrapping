import json
from bs4 import BeautifulSoup
import requests
r = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
soup = BeautifulSoup(r.content, "html.parser")
data = []

names = soup.find_all("keyword")
for name in names:
    data.append(name.text)

table = soup.find_all("td")
for item in table:
    item_text = item.text.strip()
    data.append(item_text)

with open('data.json', 'w', encoding='utf8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)
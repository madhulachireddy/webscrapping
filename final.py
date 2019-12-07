import pydoc

import pandas as pd
#import response as response

from bs4 import BeautifulSoup
import requests

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population').text
soup = BeautifulSoup(website_url, 'lxml')
My_table = soup.find('table', {'class': 'wikitable sortable'})
links = My_table.findAll('a')

with open('doc.txt', 'w') as f:
    f.write('df')

Countries=[]
list2 = range(277)
for link in links:
    Countries.append(link.get("title"))

    dilcon = list(filter(None, Countries))
    s0 = pd.Series(dilcon, name='rank''country''population''date''%of population')
    df = pd.concat([s0], axis=1)

    df = pd.DataFrame(links)
df




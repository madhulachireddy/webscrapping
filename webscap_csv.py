import csv

import requests
import rows as rows
from bs4 import BeautifulSoup

# def scrape_data(url):
# response = requests.get(url)
# soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
# filename = "scrapping.csv"
# table = soup.find('table',{'class':'wikitable sortable'})
#  print(table)


# print("testing")


# with open('scrapping.csv', 'w') as csv_file:
#  writer = csv.writer(csv_file)
#   writer.writerow(header)

#   data = [th.text.rstrip() for th in row.find_all('td')]
#  writer.writerow(data)


# if __name__ == "__main__":
#  url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
#   scrape_data(url)

from urllib.request import urlopen
from bs4 import BeautifulSoup
from unicodecsv import writer

html = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

page = urlopen(html)

data = BeautifulSoup(page, 'html.parser')

name_box = data.findAll('div',attrs={'class': "wikitable sortable"})
# edited companyName_99a4824b -> companyName__99a4824b

for i in range(len(name_box)):
    data = name_box[i].text.strip()
    for i in range(len(name_box)):
        data = name_box[i].text.strip()
        print(data)

        with open('out.csv', 'w') as csv_file:
    #write = csv.writer(csv_file)

    #for row in rows[1:]:
         #data = [th.text.rstrip() for th in row.find_all('td')]
          #writer.writerow(data)

        # next(f)
         #for line in csv_file:
          # head = []
          #value = []
         #for row in line:
           # head.append(row)

    # print(row)
    #import pandas as pd

    #df = pd.DataFrame(data)
    #print(df)

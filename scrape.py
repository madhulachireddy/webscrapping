import csv
import requests
import table as table
from Tools.demo.beer import n
from bs4 import BeautifulSoup

from scrap import population


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find_all('table')[1]

    rows = table.select('tbody > tr')

    header = [th.text.rstrip() for th in rows[0].find_all('th')]

    with open('output.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)

                for row in rows[1]:
                    data = [th.text.rstrip() for th in row.find_all('td')]
                    writer.writerow(data)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    scrape_data(url)
    import pandas as pd

    df = pd.DataFrame()
    df

# links = table.findAll('a')
#countries = [1]
#print(countries)
# for link in links:

 # print(countries)

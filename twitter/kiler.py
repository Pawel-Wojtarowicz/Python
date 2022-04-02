from bs4 import BeautifulSoup
from requests import get

URL = 'https://www.telemagazyn.pl/film/kiler-539975/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')


def download_emission_data(beautifulSoup):
    for emission in beautifulSoup.find_all('div', class_='emisje'):
        emissionDate = emission.find('span', class_='emisjaDzien').get_text()
        emissionTime = emission.find('span', class_='emisjaGodzina').get_text()
        emissionChannel = emission.find(href=True).get('href')
        emissionChannel = emissionChannel[1:-1].replace("_", " ").capitalize()

    if (emissionDate == "Dzisiaj"):
        result = f'Tak, Kiler leci o godzinie:{emissionTime} na kanale: {emissionChannel}'
    else:
        result = "Dzisiaj nie leci"

    return result

print(download_emission_data(bs))

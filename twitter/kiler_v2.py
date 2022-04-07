from bs4 import BeautifulSoup
from requests import get
import codecs
import random

URL = 'https://www.telemagazyn.pl/film/kiler-539975/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')


def random_quotes():
    with codecs.open(r"D:\Python\Git\twitter\quotes.txt", "r", "utf-8") as file:
        lines = file.read().splitlines()
        random_quote = random.sample(lines, 1)
        quote = str("\n".join(random_quote))
        return quote


def is_it_on_tv_tonight(beautifulSoup):
    emissionDays = []
    emissionHours = []
    emissionChannels = []

    for day in beautifulSoup.find_all('span', class_='emisjaDzien'):
        result = day.get_text()
        day = result.split(" ", 1)
        emissionDays.append(day[0])

    for hours in beautifulSoup.find_all('span', class_='emisjaGodzina'):
        result = hours.get_text()
        emissionHours.append(result)

    for channel in beautifulSoup.find_all('div', class_='emisjaSzczegoly'):
        results = channel.find_all(href=True)
        for result in results:
            emissionChannels.append(result.get_text())

    if emissionDays[0].startswith("Dzisiaj"):
        if (emissionDays[0] == emissionDays[2]):
            return emissionDays[0] + ' o godz:' + emissionHours[0] + ' na kanale ' + emissionChannels[0] + ' oraz o' + emissionHours[1] + ' na kanale ' + emissionChannels[1]
        elif (emissionDays[0] == "Dzisiaj"):
            return emissionDays[0] + ' o godzinie' + emissionHours[0] + ' na kanale ' + emissionChannels[0]
    else:
        return "Dzisiaj nie leci"

emission = is_it_on_tv_tonight(bs)
quote = random_quotes()

print(emission +"\n"+ "- "+quote)

from bs4 import BeautifulSoup
from requests import get

URL = 'https://www.telemagazyn.pl/film/kiler-539975/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')


def is_it_on_tv_tonight(beautifulSoup):
    emissionDays = []
    emissionHours = []
    emissionChannel = []

    for day in beautifulSoup.find_all('span', class_='emisjaDzien'):
        result = day.get_text()
        emissionDays.append(result)

    for hours in beautifulSoup.find_all('span', class_='emisjaGodzina'):
        result = hours.get_text()
        emissionHours.append(result)

    for channel in beautifulSoup.find_all('div', class_='emisjaSzczegoly'):
        results = channel.find_all(href=True)
        for result in results:
            emissionChannel.append(result.get_text())


    print("dni:", emissionDays)
    print("godziny:", emissionHours)
    print("kanaly: ", emissionChannel)
    
"""
    if (emissionDays[0] != emissionDays[1]):
        result = emissionDays[0]
        print(result)
    elif (emissionDays[0] == emissionDays[1]):
        day = emissionDays[0].split(" ", 1)

        result = day[0] + emissionHours[0] + emissionHours[1]
        print(result)
    else:
        print("Dzisiaj nie leci")
"""
is_it_on_tv_tonight(bs)

from bs4 import BeautifulSoup
from requests import get
import codecs
import random
import tweepy
import json

URL = 'https://www.telemagazyn.pl/film/kiler-539975/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')


def random_quotes():
    with codecs.open(r"D:\Python\Git\twitter\quotes.txt", "r", "utf-8") as file:
        lines = file.read().splitlines()
        random_quote = random.sample(lines, 1)
        quote = str("\n".join(random_quote))
        return quote


def is_it_on_tv_tonight(beautifulSoup, quotes):
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


    if len(emissionDays) != 0:
        if emissionDays[0].startswith("Dzisiaj"):
            if (emissionDays[0] == emissionDays[2]):
                return emissionDays[0] + ' o godz:' + emissionHours[0] + ' na kanale ' + emissionChannels[0] + ' oraz o' + emissionHours[1] + ' na kanale ' + emissionChannels[1]
            elif (emissionDays[0] == "Dzisiaj"):
                return 'Tak, o godzinie' + emissionHours[0] + ', na kanale ' + emissionChannels[0]
    else:
        return 'Dzisiaj nie leci \n\n' + '"' + quotes + '"'


def authentication(creds):

    credentials = read_creds(creds)
    api_key, api_secrets = credentials['api_key'], credentials['api_secrets']
    token, token_secrets = credentials['access_token'], credentials['access_secret']

    auth = tweepy.OAuthHandler(api_key, api_secrets)
    auth.set_access_token(token, token_secrets)

    api = tweepy.API(auth)

    status = is_it_on_tv_tonight(bs, random_quotes())
    print(status)
    api.update_status(status=status)


def read_creds(filename):

    with open(filename) as f:
        credentials = json.load(f)
    return credentials


if __name__ == '__main__':
    credentials = 'credentials.json'
    api = authentication(credentials)

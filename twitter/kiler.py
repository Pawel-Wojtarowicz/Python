from bs4 import BeautifulSoup
from requests import get
import tweepy
import json

URL = 'https://www.telemagazyn.pl/film/kiler-539975/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')


def is_it_on_tv_tonight(beautifulSoup):
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


# print(is_it_on_tv_tonight(bs))


# def main():
#     twitter_auth_keys = {
#         "consumer_key": "xxxxx",
#         "consumer_secret": "xxxxx",
#         "access_token": "xxxxx",
#         "access_token_secret": "xxxxx"
#     }

#     auth = tweepy.OAuthHandler(
#         twitter_auth_keys['consumer_key'],
#         twitter_auth_keys['consumer_secret']
#     )
#     auth.set_access_token(
#         twitter_auth_keys['access_token'],
#         twitter_auth_keys['access_token_secret']
#     )
#     api = tweepy.API(auth)

#     status = "test"
#     api.update_status(status=status)

# if __name__ == "__main__":
#     main()


def authentication(creds):

    credentials = read_creds(creds)
    api_key, api_secrets = credentials['api_key'], credentials['api_secrets']
    token, token_secrets = credentials['access_token'], credentials['access_secret']

    auth = tweepy.OAuthHandler(api_key, api_secrets)
    auth.set_access_token(token, token_secrets)

    api = tweepy.API(auth)

    status = is_it_on_tv_tonight(bs)
    api.update_status(status=status)


def read_creds(filename):

    with open(filename) as f:
        credentials = json.load(f)
    return credentials


if __name__ == '__main__':
    credentials = 'credentials.json'
    api = authentication(credentials)

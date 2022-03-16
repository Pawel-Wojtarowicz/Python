import requests
#import json

ibu = input("How many IBU at least: ")

response = requests.get(f'https://api.punkapi.com/v2/beers?ibu_gt={ibu}&per_page=5')
response_values = response.json()

if (response.status_code != requests.codes.ok):
    print("Something goes wrong")
else:
    #print(json.dumps(response.json(), indent=4))
    for i in response_values:
        print("")
        print("Id:", i['id']) 
        print("Name:", i['name']) 
        print("IBU:", i['ibu'])
        print("Tips:", i['brewers_tips']) 





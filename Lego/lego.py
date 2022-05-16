import rebrick
import json
import pprint
import webbrowser


def rebrickInit():
    # init rebrick module for general reading
    rebrick.init("8e81bf52ab2d71baadb63847e48d5035")
    try: 
        response = rebrick.lego.get_set(input("Enter LEGO number: "))
    except:
        print("Nie ma takiego zestawu.")
        exit(1)
    data = json.loads(response.read())
    return data


def get_sets(value):

    rb = rebrick.Rebrick("8e81bf52ab2d71baadb63847e48d5035", silent=True)
    result = rb.get_sets(min_pieces=value)
    for k, v in enumerate(result):
        print(f"{k+1}. {v}")


def getAlternatives(set):
    response = rebrick.lego.get_set_alternates(set['set_num'])
    alternatives = json.loads(response.read())
    return alternatives


def alternativesDict(alternatives):
    alternativesDict = {}
    for key, values in alternatives.items():
        if key == 'results':
            for url in values:
                alternativesDict[url['moc_img_url']] = url['moc_url']
            # webbrowser.open(url['moc_img_url'])
            # print(url['moc_img_url'])
            # print(url['moc_url'])
            return alternativesDict


def printAlternativeSets(alternativesDict, data):
    print(f"Alternative sets for: {data['name']}:")
    for i, (k, v) in enumerate(alternativesDict.items()):
        print(f'{i+1}. {k} - {v}')


if __name__ == '__main__':
    
    # get_sets(value=2000)
    data = rebrickInit()
    alternatives = getAlternatives(data)
    alternativesDict = alternativesDict(alternatives)
    printAlternativeSets(alternativesDict, data)

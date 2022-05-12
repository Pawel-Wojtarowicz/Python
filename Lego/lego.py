import rebrick
import json
import pprint
import webbrowser

# init rebrick module for general reading
rebrick.init("8e81bf52ab2d71baadb63847e48d5035")

response = rebrick.lego.get_set(input("Enter LEGO number: "))
data = json.loads(response.read())

response = rebrick.lego.get_set_alternates(data['set_num'])
alternatives = json.loads(response.read())

alternatives_sets = {}

for key, values in alternatives.items():
    if key == 'results':
        for url in values:
            alternatives_sets[url['moc_img_url']] = url['moc_url']
            # webbrowser.open(url['moc_img_url'])
            # print(url['moc_img_url'])
            # print(url['moc_url'])

print(f"Alternative sets for {data['name']}:")
# for key, value in alternatives_sets.items():
#     print(key, "-", value)
# print(f"Alternative sets of {response}")

for i, (k, v) in enumerate(alternatives_sets.items()):
    print(f'{i+1}. {k} - {v}')

import json

lengich = 'rus'
with open('countries.json', 'r') as json_file:
    json_data = json.load(json_file)
    print(json_data[0]['translations'][lengich]['official'])

import json
from pprint import pprint
import requests
# import pywikibot


class Сountry_in_wiki:
    def __init__(self, json_file):
        # lengich='rus',
        self.lengich = 'rus'
        self.json_data = json.load(json_file)
        self.index = -1
        self.end = len(self.json_data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index != self.end:
            # print(self.json_data[self.index]['flag'])
            country_name = self.json_data[self.index]['translations'][self.lengich]['official']

            params = {'title': country_name,
                      'printable': 'yes'}
            res = requests.get('https://ru.wikipedia.org/w/index.php', params)
            if res.status_code == 200:
                country_link = res.url
            else:
                country_link = 'Not found'
            return country_name, country_link
        else:
            raise StopIteration


with open('countries.json', 'r') as json_file:
    # json_data = Сountry_in_wiki(json_file)

    for country, link in Сountry_in_wiki(json_file):
        print(country)
        print(link)

        # cantri_name = country['translations'][lengich]['official']
        # site = 'https://ru.wikipedia.org/wiki/' + cantri_name.replace(' ', '_')
        # print(site)
        # res = requests.get(site)
        # if(res.status_code):
        #     print('ok')
        # else:
        #     print('bade')

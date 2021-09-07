import json
import requests
import csv
import os
from progress.bar import IncrementalBar
# import pywikibot


class Сountry_in_wiki:
    '''
    для тестового запуска лучше всего self.end = len(self.json_data) 
    не раскомментировать иначе программа будет прогонять все 250 стран,
    в сренем это занимает где-то минут 5
    '''

    def __init__(self, json_file):
        '''
        '''
        self.json_data = json.load(json_file)
        self.index = -1
        self.end = 50
        # self.end = len(self.json_data)
        self.bar = IncrementalBar('Countdown', max=self.end)

    def __iter__(self):
        return self

    def __next__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.bar.next()
        self.index += 1
        if self.index != self.end:
            # print(self.json_data[self.index]['flag'])
            country_name = self.json_data[self.index]['name']['official']

            params = {'title': country_name, }
            res = requests.get('https://en.wikipedia.org/w/index.php', params)
            if res.status_code == 200:
                country_link = res.url
            else:
                country_link = 'Not found'
            return country_name, country_link
        else:
            self.bar.finish()
            raise StopIteration


if __name__ == '__main__':
    with open('countries.json', 'r', encoding='utf-8') as json_file:
        # json_data = Сountry_in_wiki(json_file)
        with open("country_links.csv", "w") as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows([['country', 'link']])

        for country, link in Сountry_in_wiki(json_file):
            print(country)
            print(link)

            with open("country_links.csv", "a", newline='', encoding='utf-8') as f:
                datawriter = csv.writer(f, delimiter=',')
                datawriter.writerows([[country, link]])

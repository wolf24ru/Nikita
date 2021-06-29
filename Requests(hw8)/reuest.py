import requests


def intelligence(super_hero_name):
    search_url = 'https://superheroapi.com/api/2619421814940190/search/'
    result_requests = requests.get(search_url + super_hero_name)
    num = 1
    super_dict = {}

    if result_requests.json().get('response') == 'success':
        hero_json = result_requests.json()
        for x in hero_json.get('results'):

            #---------------- !!!переписать под опредления четого имени!!!!----------

            print(f'{num} {x.get("name")}')
            super_dict.update({num: x.get("id")})
            num += 1
        # num_hero = input('\nВыберите необходимого супер героя:')
        num_hero = 1
        for i in hero_json.get('results'):
            if i.get('id') == super_dict.get(num_hero):
                return(int(i.get('powerstats').get('intelligence')))
    else:
        print(f'Герой {super_hero_name} не найден')
        return 0


if __name__ == '__main__':
    super_heros_names = ['Hulk', 'Captain America', 'Thanos']
    # for x in super_heros_names:
    #     intelligence(x)
    p = intelligence('Hulk')

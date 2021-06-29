import requests


def intelligence(super_hero_name):
    search_url = 'https://superheroapi.com/api/2619421814940190/search/'
    result_requests = requests.get(search_url + super_hero_name)
    hero_json = result_requests.json()
    if hero_json.get('response') == 'success':

        for hero in hero_json.get('results'):
            if hero.get('name') == super_hero_name:
                return int(hero.get('powerstats').get('intelligence'))
            else:
                print('Error 404\nThe hero was not found')
                return 0
    else:
        print(f'Герой {super_hero_name} не найден')
        return 0


if __name__ == '__main__':
    super_heros = {'Hulk': {}, 'Captain America': {}, 'Thanos': {}}

    for name in super_heros:
        super_heros[name].update({'intelligence': intelligence(name)})

    the_smartest_hero = sorted(super_heros.items(),
                               key=lambda smart: smart[1].get('intelligence'),
                               reverse=True)
    print(f'Самый умный герой: {the_smartest_hero[0][0]}')

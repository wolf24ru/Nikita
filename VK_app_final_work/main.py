# 9eddd1dcca6f914f1d11940be62bdad285eda0a22e5dd3d0109aef0a05c0986f46e31cf00560dd34e3152

import requests
from pprint import pprint


class FotoUpdate():
    def __init__(self, vk_token):
        self.vk_token = vk_token
        # self.owner_id = owner_vk_id
        # self.ya_token = ya_token

    def photos_get(self, owner_id):
        params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'count': 2,
            'access_token': self.vk_token,
            'v': 5.77
        }
        href = requests.get('https://api.vk.com/method/photos.get', params).json()
        for photo in href['response']['items']:
            print(photo['sizes'][-1]['url'])
        return href


if __name__ == '__main__':
    TOKEN = '9eddd1dcca6f914f1d11940be62bdad285eda0a22e5dd3d0109aef0a05c0986f46e31cf00560dd34e3152'
    f = FotoUpdate(TOKEN)

    f.photos_get(67079934)

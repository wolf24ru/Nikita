import requests


class Insta_API:
    def __init__(self, code):
        self.token = code

    def get_photo(self, limit):
        '''получение поледних нескольких фото
        Keyword arguments:
         limit -- количество фотографий
        return:
        {'id': id картинки;
         'media_url': ссылка на картинку
        }

        '''
        params = {
            'fields': 'id,media_url',
            'access_token': self.token,
            'limit': limit
        }
        re = requests.get(
            'https://graph.instagram.com/me/media', params).json()
        return re

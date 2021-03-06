import requests


class FotoUpdate():
    def __init__(self, vk_token):
        self.vk_token = vk_token
        # self.owner_id = owner_vk_id

    def photos_profile_get(self, owner_id, album_id, count):
        '''Получение фотографий пользователя
        Keyword arguments:
        owner_id -- id пользователя
        count -- количество возвращаеммых фотографиий
        return:
        [{file_name: Название фотографии,
          size: размер вотографии,
          url: ссылка на фотографию
          }]

        '''
        resul_link_dict = []
        params = {
            'owner_id': owner_id,
            'album_id': album_id,
            'count': count,
            'extended': 1,
            'lang ': 0,
            'access_token': self.vk_token,
            'v': 5.77,

        }
        href = requests.get(
            'https://api.vk.com/method/photos.get', params).json()
        for photo in href['response']['items']:
            resul_link_dict += [{'file_name': f'{photo["likes"]["count"]}.jpg',
                                 'size': photo['sizes'][-1]['type'],
                                 'url': photo['sizes'][-1]['url']}]

        return resul_link_dict

    def albums_dict(self, owner_id):
        '''Получение всех альбомов пользователя
        Keyword arguments:
        owner_id -- id пользователя ВК к альбомам которого у вас есть доступ
        return:
        {id_альбома: название_фльбома}

        '''
        resul_link_dict = {}
        params = {
            'owner_id': owner_id,
            'need_system': 1,
            'lang ': 0,
            'access_token': self.vk_token,
            'v':  '5.30',
        }
        req = requests.get(
            'https://api.vk.com/method/photos.getAlbums', params).json()
        for aldum in req['response']['items']:
            resul_link_dict.update({aldum['id']: aldum['title']})
        return resul_link_dict

        def getLongPollServer(self, group_id):
            params = {
            'group_id': group_id,
            'v': 5.131
            }
            return req = requests.get(
                'https://api.vk.com/method/groups.getLongPollServer', params).json()

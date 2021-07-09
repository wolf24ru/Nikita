import requests


class Insta_API:
    def __init__(self, code):
    	self.token = code
        # params = {
        #     'client_id': 1475772392761405,
        #     'client_secret': '987eea46cea06f67452e7c611fb8fb3f',
        #     'grant_type': 'authorization_code',
        #     'redirect_uri': 'https://socialsizzle.herokuapp.com/auth/',
        #     'code': code
        # }
        # r = requests.post(
        #     'https://api.instagram.com/oauth/access_token', params)
        # print(r)
        # if r.status_code == 200:
        #     self.token = r.json()['access_token']
        # else:
        #     print('Ошибка получения токена')
        #     self.token = 0

    def get_photo(self, limit):
        params = {
            'fields': 'id,media_url',
            'access_token': self.token,
            'limit': limit
        }
        re = requests.get(
            'https://graph.instagram.com/me/media', params).json()
        return re

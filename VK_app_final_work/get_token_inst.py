import requests
import sys

params = {
    'client_id':'ID приложения Instagram' ,
    'client_secret': 'Секрет приложения Instagram',
    'grant_type': 'authorization_code',
    'redirect_uri': 'URI перенаправления, переданный при переходе пользователя к окну авторизации. URI должны совпадать',
    'code': 'Код авторизации, переданный в параметре code'
}

r = requests.post('https://api.instagram.com/oauth/access_token', params)

if r.status_code == 200:
    print()
    print(r.json()['access_token'])
else:
    print()
    print(r.json()['error_message'])


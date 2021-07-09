import requests
import sys

params = {
    'client_id': 1475772392761405,
    'client_secret': '987eea46cea06f67452e7c611fb8fb3f',
    'grant_type': 'authorization_code',
    'redirect_uri': 'https://socialsizzle.herokuapp.com/auth/',
    'code': sys.argv[1]
}

r = requests.post('https://api.instagram.com/oauth/access_token', params)

if r.status_code == 200:
    print()
    print(r.json()['access_token'])
else:
    print()
    print(r.json()['error_message'])


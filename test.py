
# from DPM1Standart import DPM1Standart


# def readx(width):
#     w = width.get('бла-бла')
#     return w


# if __name__ == '__main__':
# 	width = {'какая-то_херня': 123,
# 	'тут_тоже': 456}
	
#     DPM1Standart(readx(width))
import requests


if __name__ == '__main__'(cod):
    params = {
        'client_id': 1475772392761405,
        'client_secret': '987eea46cea06f67452e7c611fb8fb3f',
        'grant_type': 'authorization_code',
        'redirect_uri': 'https://socialsizzle.herokuapp.com/auth/',
        'code': cod
    }

    r = requests.post('https://api.instagram.com/oauth/access_token', params)
    print(r.json())
    print('\n\n')
    print()

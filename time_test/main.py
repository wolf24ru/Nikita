https://oauth.vk.com/authorize?client_id=7895500&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=pages&response_type=token&v=5.131
import json
from pprint import pprint
from VK import FotoUpdate
TOKEN_VK = ''
vk = FotoUpdate(TOKEN_VK)
p =vk.sm()
# res = p['response']['items']
# sr = sorted(res, key = lambda item: (item['likes']['count'], item['comments']['count']),reverse=True)[:3]
# sr = [link['sizes'][-1]['url'] for link in sorted(res, key = lambda item: (item['likes']['count'], item['comments']['count']),reverse=True)[:3]]
# pprint(res)
# print(f'================={len(res)}=================')
pprint(p)



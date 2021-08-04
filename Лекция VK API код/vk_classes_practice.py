#!/usr/bin/env python
# coding: utf-8

# Создаем приложение

#
# 1) Нажимаете на кнопку создать приложение
#
# 2) Выбираете standalone приложение, указываете название приложения
#
# ![](https://sun9-60.userapi.com/c857736/v857736671/14acdc/66pnWpKHRmM.jpg)
#
# 3) Переходите в настройки, включаете Open API
#
# 4) В поле *адрес сайта* вводите http://localhost
#
# 5) В поле базовый домен вводите localhost
#
# ![](https://sun9-4.userapi.com/c857736/v857736671/14acee/6qdLYkpdBl4.jpg)
#
# 6) Сохраняете изменения
#
# 7) Копируете id приложения
#
# 8) В ссылку
#
# https://oauth.vk.com/authorize?client_id=1&display=page&scope=stats,offline&response_type=token&v=5.131
#
#
#
# вместо 1 вставьте id **вашего** приложения. Не забудьте указать scope: https://vk.com/dev/permissions
#
# 9) Нажимаете разрешить
#
# 10) Сохраняете токен
#
# ![](https://sun9-29.userapi.com/c857736/v857736671/14acf8/2c-F9g7w0jA.jpg)

# In[2]:


# читаем токен
with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()


# **Синтаксис любого запроса**
# https://vk.com/dev/api_requests
#
# **Методы**
# https://vk.com/dev/methods
#
# **Версии**
# https://vk.com/dev/versions
#
# **Об ограничениях**
# https://vk.com/dev/api_requests?f=3.%20%D0%9E%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8

# Получим базовую информацию о пользователе при помощи [users.get](https://vk.com/dev/users.get)

# In[3]:


import requests
from pprint import pprint

URL = 'https://api.vk.com/method/users.get'
params = {
    'user_id': '1',
    # токен и версия api являются обязательными параметрами во всех запросах к vk
    'access_token': token,
    'v': '5.131'
}
res = requests.get(URL, params=params)
pprint(res.json())


# Получим дополнительно еще какие-то поля

# In[14]:


params = {
    'user_id': '1',
    'access_token': token,
    'v': '5.131',
    'fields': 'education,sex'
}
res = requests.get(URL, params)
pprint(res.json())


# Напишем функцию, которая будет находить группы по поисковому запросу при помощи метода [groups.search](https://vk.com/dev/groups.search)

# In[7]:


def search_groups(q, sorting=0):
    '''
    Параметры sort
    0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);
    1 — сортировать по скорости роста;
    2 — сортировать по отношению дневной посещаемости к количеству пользователей;
    3 — сортировать по отношению количества лайков к количеству пользователей;
    4 — сортировать по отношению количества комментариев к количеству пользователей;
    5 — сортировать по отношению количества записей в обсуждениях к количеству пользователей.        
    '''
    params = {
        'q': q,
        'access_token': token,
        'v': '5.131',
        'sort': sorting,
        'count': 300
    }
    req = requests.get(
        'https://api.vk.com/method/groups.search', params).json()
#     print(req)
    req = req['response']['items']
    return req


target_groups = search_groups('python')
pprint(target_groups)


# Получим расширенную информацию по группам при помощи метода [groups.getById](https://vk.com/dev/groups.getById)

# In[8]:


# преобразуем список всех id в строку (в таком виде принимает данные параметр fields)
target_group_ids = ','.join([str(group['id']) for group in target_groups])
pprint(target_group_ids)


# In[9]:


params = {
    'access_token': token,
    'v': '5.131',
    'group_ids': target_group_ids,
    'fields': 'members_count,activity,description'

}
req = requests.get('https://api.vk.com/method/groups.getById', params)

pprint(req.json()['response'])


# Если строим какую-то сложную логику взаимодействия с API, то логично будет инкапсулировать весь нужный функционал в класс. Какие нам нужны данные, чтобы инициализировать класс?

# In[ ]:


# In[ ]:


# In[ ]:


# In[16]:


# токен и версия могут быть разные в разных экзмеплярах
class VkUser:
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }


# In[17]:


# базовый URL будет всегда один, в инициализации он не нужен
class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }


# In[22]:


# перенесем в класс ранее написанный функционал
class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def search_groups(self, q, sorting=0):
        '''
        Параметры sort
        0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);
        1 — сортировать по скорости роста;
        2 — сортировать по отношению дневной посещаемости к количеству пользователей;
        3 — сортировать по отношению количества лайков к количеству пользователей;
        4 — сортировать по отношению количества комментариев к количеству пользователей;
        5 — сортировать по отношению количества записей в обсуждениях к количеству пользователей.        
        '''
        group_search_url = self.url + 'groups.search'
        group_search_params = {
            'q': q,
            'sort': sorting,
            'count': 300
        }
        req = requests.get(group_search_url, params={
                           **self.params, **group_search_params}).json()
        return req['response']['items']

    def search_groups_ext(self, q, sorting=0):
        group_search_ext_url = self.url + 'groups.getById'
        target_groups = self.search_groups(q, sorting)
        target_group_ids = ','.join([str(group['id'])
                                     for group in target_groups])
        groups_info_params = {
            'group_ids': target_group_ids,
            'fields': 'members_count,activity,description'
        }
        req = requests.get(group_search_ext_url, params={
                           **self.params, **groups_info_params}).json()
        return req['response']


# In[23]:


# проверяем
vk_client = VkUser(token, '5.131')


# In[24]:


pprint(vk_client.search_groups('python'))


# In[25]:


pprint(vk_client.search_groups_ext('python'))


# In[27]:


# import pandas as pd
# pd.DataFrame(vk_client.search_groups_ext('python'))


# Добавим метод для получения подписчиков при помощи [users.getFollowers](https://vk.com/dev/users.getFollowers)

# In[30]:


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def search_groups(self, q, sorting=0):
        '''
        Параметры sort
        0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);
        1 — сортировать по скорости роста;
        2 — сортировать по отношению дневной посещаемости к количеству пользователей;
        3 — сортировать по отношению количества лайков к количеству пользователей;
        4 — сортировать по отношению количества комментариев к количеству пользователей;
        5 — сортировать по отношению количества записей в обсуждениях к количеству пользователей.        
        '''
        group_search_url = self.url + 'groups.search'
        group_search_params = {
            'q': q,
            'sort': sorting,
            'count': 300
        }
        req = requests.get(group_search_url, params={
                           **params, **group_search_params}).json()
        return req['response']['items']

    def search_groups_ext(self, q, sorting=0):
        group_search_ext_url = self.url + 'groups.getById'
        target_groups = self.search_groups(q, sorting)
        target_group_ids = ','.join([str(group['id'])
                                     for group in target_groups])
        groups_info_params = {
            'group_ids': target_group_ids,
            'fields': 'members_count,activity,description'
        }
        req = requests.get(group_search_ext_url, params={
                           **params, **groups_info_params}).json()
        return req['respone']

    def get_followers(self, user_id=None):
        followers_url = self.url + 'users.getFollowers'
        followers_params = {
            'count': 1000,
            'user_id': user_id
        }
        res = requests.get(followers_url, params={
                           **self.params, **followers_params}).json()
        return res['response']


# In[31]:


# получим своих подписчиков
vk_client = VkUser(token, '5.131')
vk_client.get_followers()


# In[32]:


# получим подписчиков другого пользователя
vk_client = VkUser(token, '5.131')
vk_client.get_followers('1')


# Создадим метод для получения групп пользователя при помощи [groups.get](https://vk.com/dev/groups.get)

# In[33]:


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def search_groups(self, q, sorting=0):
        '''
        Параметры sort
        0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);
        1 — сортировать по скорости роста;
        2 — сортировать по отношению дневной посещаемости к количеству пользователей;
        3 — сортировать по отношению количества лайков к количеству пользователей;
        4 — сортировать по отношению количества комментариев к количеству пользователей;
        5 — сортировать по отношению количества записей в обсуждениях к количеству пользователей.        
        '''
        group_search_url = self.url + 'groups.search'
        group_search_params = {
            'q': q,
            'sort': sorting,
            'count': 300
        }
        req = requests.get(group_search_url, params={
                           **params, **group_search_params}).json()
        return req['response']['items']

    def search_groups_ext(self, q, sorting=0):
        group_search_ext_url = self.url + 'groups.getById'
        target_groups = self.search_groups(q, sorting)
        target_group_ids = ','.join([str(group['id'])
                                     for group in target_groups])
        groups_info_params = {
            'group_ids': target_group_ids,
            'fields': 'members_count,activity,description'
        }
        req = requests.get(group_search_ext_url, params={
                           **params, **groups_info_params}).json()
        return req['respone']

    def get_followers(self, user_id=None):
        followers_url = self.url + 'users.getFollowers'
        followers_params = {
            'count': 1000,
            'user_id': user_id
        }
        res = requests.get(followers_url, params={
                           **self.params, **followers_params}).json()
        return res['response']['items']

    def get_groups(self, user_id=None):
        groups_url = self.url + 'groups.get'
        groups_params = {
            'count': 1000,
            'user_id': user_id,
            'extended': 1,
            'fields': 'members_count'
        }
        res = requests.get(groups_url, params={**params, **groups_params})
        return res.json()


# In[34]:



# получим свои группы
vk_client = VkUser(token, '5.131')
vk_client.get_groups()


# In[35]:


# получим группы другого пользователя
vk_client = VkUser(token, '5.131')
vk_client.get_groups('1')


# Теперь мы можем импортировать этот класс в другие программы и использовать его интерфейс для реализации нужной логики

# In[ ]:

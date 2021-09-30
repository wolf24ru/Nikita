# Подключение к ВК групе
TOKEN_VK_GROUP = '3205c71e7b40a49f76212f837948cc30732790d54bc5f7c446c458d201ebae6810281418b979888ad9eb0'
GROUP_ID = 207491288

import random
import vk_api
import requests
from VK_class import VK_bot
from VKinder_db import VKinder_db
from urllib.parse import urlparse


def person_find(vk_connect, db_connect, user_id: int, request_dict: object) -> dict:
    # получить человека по заданным параметрам
    search_users = vk_connect.user_session.get_api().users.search(
        count=1000,
        city=vk_connect.search_city_id(request_dict.city),
        country=1,
        age_from=request_dict.age_from,
        age_to=request_dict.age_to,
        sex=request_dict.sex,
        status=request_dict.marital_status,
        fields='domain'
    )['items']
    # из полученного списка рендомно выбрать  человека
    user_for_you = random.choice(search_users)

    if not db_connect.check_user_search(user_for_you['id']):
        # Получить 3 фото удовлетворяющие запросу
        try:
            photos_user_all = vk_connect.user_session.get_api().photos.get(
                owner_id=user_for_you['id'],
                album_id='profile',
                extended=1,
                count=100,
            )['items']
        except vk_api.exceptions.ApiError:
            return person_find(vk_connect, db_connect, user_id, request_dict)

        link_photo = [link['sizes'][-1]['url'] for link in
                      sorted(photos_user_all, key=lambda item: (item['likes']['count'], item['comments']['count']),
                             reverse=True)[:3]]
        # получить ссылку
        # сообщение с человеком, сообщение с топ-3 фото
        url_profile = f'https://vk.com/{user_for_you["domain"]}'
        profile = f'@{user_for_you["domain"]}({user_for_you["first_name"]})'
        vk_connect.send_msg(message=f'Я нашел для тебя {profile}',
                            user_id=user_id,
                            )

        for photo in link_photo:
            re = requests.get(photo, stream=True)
            vk_connect.photo_upload.photo_messages(re.raw, event.peer_id)
            # vk_connect.send_msg(message=photo,
            #                     user_id=user_id
            #                     )
        vk_connect.keyboard_new.get_keyboard()
        return {
            'person_id': user_for_you['id'],
            'user_name': user_for_you["first_name"],
            'url_profile': url_profile,
            'link_photo': link_photo
        }
    else:
        return person_find(vk_connect, user_id, request_dict)


def take_token(vk_connect: object, id_user: str):
    # Пишет сообщение о том что ему нужен доступ
    vk_connect.send_msg(message=f'Один маленький нюанс. Для полноценнной работы мне нужно твое разершение.\n'
                                f'А так как я чат бот, перенаправлять тебя на другие источники я не могу.\n'
                                f'Так что мне нужна твоя помощь\n'
                                f'\n'
                                f'Для этого перейди по этой ссылке:\n'
                                f'\nhttps://oauth.vk.com/authorize?client_id=7895500&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=pages&response_type=token&v=5.131\n'
                                f'\nСкопируй то что будет в адресной страке и отправь мне\n'
                                f'Я жду!',
                        user_id=id_user
                        )
    url = urlparse(vk_connect.listen_dialog()[1].text)
    params_one = url.fragment.split(';')
    params = [i.split('&')[0] for i in params_one]
    params_dict = {i.split('=')[0]: i.split('=')[1] for i in params}
    if params_dict:
        vk_connect.user_auoth(params_dict['access_token'])

    # и подключается к данными пользваотедля


if __name__ == '__main__':
    vk_connect = VK_bot(GROUP_ID, TOKEN_VK_GROUP)
    # Подключение к БД
    db_connect = VKinder_db('vk', '12345678', 'vkinder_db')
    # db_connect.new_db()
    request_dict = object
    # comand_dict ={
    #     'Начать':1,
    #     'Поиск':1,
    #     'Изменить запрос':1
    # }
    while True:
        listen_list = vk_connect.listen_dialog()
        user_info = listen_list[0]
        event = listen_list[1]
        user_name = user_info[0]['first_name']
        if event.text == 'Начать' and event.from_user:
            take_token(vk_connect, event.user_id)
            # проверка на нового пользователя
            # если пользователь новый
            if db_connect.check_new_user(event.user_id, user_name):
                vk_connect.send_msg(message=f'Отилчно! {user_name}, ну что попробуем найти тебе пару?\n'
                                            f'Для начала давай настроим поиск!',
                                    user_id=event.user_id
                                    )
                request_dict = vk_connect.new_user_search(event.user_id)
                # Отобразить клавиатура с сообщением  'Давай еще раз все проверим'

                #     варианты кнопок: "все верно, начать поиск" "изменить запрос"
                db_connect.add_request(event.user_id,
                                       request_dict['age_from'],
                                       request_dict['age_to'],
                                       request_dict['sex'],
                                       request_dict['city'],
                                       request_dict['marital_status'])
                vk_connect.send_msg(message=f'Ну а теперь мы можем попытаться найти того кто покорит твое сердце!\n'
                                            f'жмякай кнопку "Поиск" и приступим',
                                    user_id=event.user_id,
                                    keyboard=vk_connect.keyboard_old.get_keyboard()
                                    )
            # Если пользователь уже есть в базе
            else:
                vk_connect.send_msg(message=f'Рад тебя снова видеть, {user_name}.\n'
                                            f'Ну что попробуем найти тебе пару?',
                                    user_id=event.user_id,
                                    keyboard=vk_connect.keyboard_old.get_keyboard()
                                    )
                # проверка на наличе запроса от пользователя
                request_dict = db_connect.last_request(event.user_id)
                text = vk_connect.listen_dialog()[1].text
        elif event.text == 'Поиск' and event.from_user:
            request_dict = db_connect.last_request(event.user_id)
            if request_dict:
                person = person_find(vk_connect, db_connect, event.user_id, request_dict)

                db_connect.add_search(
                    person['person_id'],
                    event.user_id
                )

                # request_dict['city']
                # Выполнить поиск по старым запросам
            else:
                vk_connect.send_msg(message=f'Я тут заметил что у тебя не настроен фильтр поиска.\n'
                                            f'Давай изменим это!',
                                    user_id=event.user_id
                                    )
                request_dict = vk_connect.new_user_search(event.user_id)
                person = person_find(vk_connect, db_connect, event.user_id, request_dict)
                db_connect.add_request(
                    event.user_id,
                    request_dict['age_from'],
                    request_dict['age_to'],
                    request_dict['sex'],
                    request_dict['city'],
                    request_dict['marital_status']
                )

                # начать отсюда. тут надо добавить обработчик поиска и проверку на наличие существующего запроса

        elif event.text == 'Изменить запрос' and event.from_user:
            vk_connect.send_msg(message='Что меняем?',
                                user_id=event.user_id,
                                keyboard=vk_connect.keyboard_request.get_keyboard())
        elif event.text == 'Всё верно' and event.from_user:
            vk_connect.send_msg(user_id=event.user_id,
                                keyboard=vk_connect.keyboard_old.get_keyboard(),
                                message='Отлично, постораюсь не забыть твои предпочтения😉'
                                )

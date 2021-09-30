# Подключение к ВК групе
TOKEN_VK_GROUP = '3205c71e7b40a49f76212f837948cc30732790d54bc5f7c446c458d201ebae6810281418b979888ad9eb0'
GROUP_ID = 207491288

import random
from VK_class import VK_bot
from VKinder_db import VKinder_db

def person_find(vk_connect, user_id: int, request_dict: dict) -> dict:

    # получить человека по заданным параметрам
    search_users = vk_connect.vk_session.get_api().users.search(
        count=1000,
        city=vk_connect.search_city_id(request_dict['city']),
        country=1,
        age_from=request_dict['age_from'],
        age_to=request_dict['age_to'],
        sex=request_dict['sex'],
        status=request_dict['marital_status'],
        fields='domain'
    )['items']
    # из полученного списка рендомно выбрать  человека
    user_for_you = random.choice(search_users)
    # Получить 3 фото удовлетворяющие запросу
    photos_user_all = vk_connect.vk_session.get_api().photos.get(
        owner_id=user_for_you['id'],
        album_id='profile',
        extended=1,
        count=100,
    )['items']
    link_photo = [link['sizes'][-1]['url'] for link in
                  sorted(photos_user_all, key=lambda item: (item['likes']['count'], item['comments']['count']),
                         reverse=True)[:3]]
    # получить ссылку
    # сообщение с человеком, сообщение с топ-3 фото
    url_profile = f'https://vk.com/{user_for_you["domain"]}'
    profile = f'@{user_for_you["domain"]}({user_for_you["first_name"]})'
    vk_connect.send_msg(message=f'Я нашел для тебя {profile}',
                        user_id=event.user_id,
                        )
    for photo in link_photo:
        vk_connect.send_msg(message=photo,
                            user_id=event.user_id
                            )
    vk_connect.keyboard_new.get_keyboard()
    return {
        'person_id': user_for_you['id'],
        'user_name': user_for_you["first_name"],
        'url_profile': url_profile,
        'link_photo': link_photo
    }

def take_token(id_user: str):
    pass
    # функция просит токен
    # и подключается к данными пользваотедля
if __name__ == '__main__':
    vk_connect = VK_bot(GROUP_ID, TOKEN_VK_GROUP)
    # Подключение к БД
    db_connect = VKinder_db('vk', '12345678', 'vkinder_db')
    # db_connect.new_db()

    while True:
        listen_list = vk_connect.listen_dialog()
        user_info = listen_list[0]
        event = listen_list[1]
        user_name = user_info[0]['first_name']
        if event.text == 'Начать' and event.from_user:
            # проверка на нового пользователя
            # если пользователь новый
            if db_connect.check_new_user(event.user_id, user_name):
                vk_connect.send_msg(message=f'Здравствуй, {user_name}. Ну что попробуем найти тебе пару?\n'
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
                if text == 'Поиск':
                    if request_dict:
                        print(request_dict)
                        person = person_find(vk_connect, event.user_id, request_dict)
                        db_connect.add_request(
                            event.user_id,
                            request_dict['age_from'],
                            request_dict['age_to'],
                            request_dict['sex'],
                            request_dict['city'],
                            request_dict['marital_status']
                        )
                        # request_dict['city']
                        # Выполнить поиск по старым запросам
                    else:
                        vk_connect.send_msg(message=f'Я тут заметил что у тебя не настроен фильтр поиска.\n'
                                                    f'Давай изменим это!',
                                            user_id=event.user_id
                                            )
                        request_dict = vk_connect.new_user_search(event.user_id)
                        person = person_find(vk_connect, event.user_id, request_dict)
                        db_connect.add_request(
                            event.user_id,
                            request_dict['age_from'],
                            request_dict['age_to'],
                            request_dict['sex'],
                            request_dict['city'],
                            request_dict['marital_status']
                        )
                elif text == 'Изменить запрос':
                    pass
                else:
                    pass

                # начать отсюда. тут надо добавить обработчик поиска и проверку на наличие существующего запроса

        elif event.text == 'Изменить запрос' and event.from_user:
            vk_connect.send_msg(message='Что меняем?',
                                user_id=event.user_id,
                                keyboard=vk_connect.keyboard_request.get_keyboard())
        elif event.text == 'Всё верно' and event.from_user:
            vk_connect.send_msg(user_id=event.user_id,
                                keyboard=vk_connect.keyboard_new.get_keyboard(),
                                message='Отлично, постораюсь не забыть твои предпочтения😉'
                                )

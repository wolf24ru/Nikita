# Подключение к ВК групе
TOKEN_VK_GROUP = '3205c71e7b40a49f76212f837948cc30732790d54bc5f7c446c458d201ebae6810281418b979888ad9eb0'
GROUP_ID = 207491288

from VK_class import VK_bot
from VKinder_db import VKinder_db

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
            if db_connect.checking_new_user(event.user_id, user_name):
                vk_connect.send_msg(message=f'Здравствуй, {user_name}. Ну что попробуем найти тебе пару?\n'
                                            f'Для начала давай настроим поиск!',
                                    user_id=event.user_id
                                    )
                new_request_dict = vk_connect.new_user_search(event.user_id)
                # Отобразить клавиатура с сообщением  'Давай ещще раз все проверим'
                #     варианты кнопок: "все верно, начать поиск" "изменить запрос"


                db_connect.add_request(event.user_id,
                                       new_request_dict['age'],
                                       new_request_dict['sex'],
                                       new_request_dict['city'],
                                       new_request_dict['marital_status'])

            # Если пользователь уже есть в базе
            else:
                vk_connect.send_msg(message=f'Рад тебя снова видеть, {user_name}.\n'
                                            f'Ну что попробуем найти тебе пару?',
                                    user_id=event.user_id,
                                    keyboard=vk_connect.keyboard_old.get_keyboard()
                                    )
                !# начать отсюда. тут надо добавить обработчик поиска и проверку на наличие существующего запроса

        elif event.text == 'Изменить запрос' and event.from_user:
            vk_connect.send_msg(message='Что меняем?',
                                user_id=event.user_id,
                                keyboard=vk_connect.keyboard_request.get_keyboard())
        elif event.text == 'Всё верно' and event.from_user:
            vk_connect.send_msg(user_id=event.user_id,
                                keyboard=vk_connect.keyboard_new.get_keyboard(),
                                message='Отлично, постораюсь не забыть твои предпочтения😉'
                                )

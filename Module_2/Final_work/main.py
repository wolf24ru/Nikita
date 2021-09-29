# Подключение к ВК групе
TOKEN_VK_GROUP = '3205c71e7b40a49f76212f837948cc30732790d54bc5f7c446c458d201ebae6810281418b979888ad9eb0'
GROUP_ID = 207491288

from VK_class import VK_bot
from VKinder_db import VKinder_db

if __name__ == '__main__':
    vk_connect = VK_bot(GROUP_ID, TOKEN_VK_GROUP)
    # Подключение к БД
    db_connect = VKinder_db('vk', '12345678', 'vkinder_db')
    db_connect.new_db()

    while True:
        listen_list = vk_connect.listen_dialog()
        user_info = listen_list[0]
        event = listen_list[1]
        if event.text == 'Начать':
            # проверка на нового пользователя

            if event.from_user:
                # если пользователь новый
                user_name = user_info[0]['first_name']
                # Добавление Пользователя в БД

                vk_connect.send_msg(message=f'Здравствуй, {user_name}. Ну что попробуем найти тебе пару?\n'
                                            f'Для начала давай настроим поиск!', user_id=event.user_id
                                    )

                # если пользователь уже есть в базе
                # vk_connect.send_msg(message=f'Рад тебя снова видеть, {user_name}.\n'
                #                             f'Ну что попробуем найти тебе пару?',
                #                     user_id=event.user_id,
                #                     keyboard=vk_connect.keyboard_old.get_keyboard()
                #                     )

        elif event.text == 'Изменить запрос':
            if event.from_user:
                vk_connect.send_msg(message='Что меняем?',
                                    user_id=event.user_id,
                                    keyboard=vk_connect.keyboard_request.get_keyboard())
        elif event.text == 'Всё верно':
            if event.from_user:
                vk_connect.send_msg(user_id=event.user_id,
                                    keyboard=vk_connect.keyboard_new.get_keyboard(),
                                    message='Отлично, постораюсь не забыть твои предпочтения😉'
                                    )

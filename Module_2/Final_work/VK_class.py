import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from VKAuth.vkauth import VKAuth
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

token_vk_grup = '3205c71e7b40a49f76212f837948cc30732790d54bc5f7c446c458d201ebae6810281418b979888ad9eb0'
vk_session = vk_api.VkApi(token=token_vk_grup)
longpoll = VkBotLongPoll(vk_session, 207491288)
vk = vk_session.get_api()

# Тут подключение к БД

lslongpooll = VkLongPoll(vk_session)
lsvk = vk_session.get_api()

keyboard_new = VkKeyboard(one_time=False)
keyboard_new.add_button('Начать', color=VkKeyboardColor.POSITIVE)

keyboard_old = VkKeyboard(one_time=False)
keyboard_old.add_button('Начать', color=VkKeyboardColor.POSITIVE)
keyboard_old.add_button('Изменить запрос', color=VkKeyboardColor.PRIMARY)


keyboard_request = VkKeyboard(one_time=False)
keyboard_request.add_button('Изменить возраст', color=VkKeyboardColor.SECONDARY)
keyboard_request.add_button('Изменить пол', color=VkKeyboardColor.SECONDARY)
keyboard_request.add_line()
keyboard_request.add_button('Изменить город', color=VkKeyboardColor.SECONDARY)
keyboard_request.add_button('Изменить положение', color=VkKeyboardColor.SECONDARY)
keyboard_request.add_line()
keyboard_request.add_button('Выйти', color=VkKeyboardColor.NEGATIVE)

is_new_user = True


keyboard_new.get_keyboard()
for event in lslongpooll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        user_info = lsvk.users.get(
            user_ids=event.user_id,
            fields='sex,city,'
        )
        # проверка на нового пользователя

        print(event.text)
        if event.text == 'Начать':
            if event.from_user:
                user_name = user_info[0]['first_name']
                lsvk.messages.send(
                    user_id=event.user_id,
                    message=f'Здравствуй, {user_name}. Ну что попробуем найти тебе пару?\n'
                            f'Для начала давай настроим поиск!',
                    random_id=get_random_id()
                    )

        if event.text == 'Изменить запрос':
            if event.from_user:
                lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard_request.get_keyboard(),
                    message='Что меняем?'
                    )
        if event.text == 'Выйти':
            if event.from_user:
                lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard_new.get_keyboard(),
                    message='Выходим из настроек'
                )
        if event.text == 'id':
            if event.from_user:
                lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=f'{event.user_id}'
                )
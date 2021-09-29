import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType


class VK_bot:
    def __init__(self, group_id: int, token_vk_group: str):
        self.token_vk_group = token_vk_group
        self.vk_session = vk_api.VkApi(token=self.token_vk_group)
        self.longpoll = VkBotLongPoll(self.vk_session, group_id)
        # self.vk = self.vk_session.get_api()

        self.keyboard_new = VkKeyboard(one_time=False)
        self.keyboard_new.add_button('Начать', color=VkKeyboardColor.POSITIVE)

        self.keyboard_old = VkKeyboard(one_time=False)
        self.keyboard_old.add_button('Поиск', color=VkKeyboardColor.POSITIVE)
        self.keyboard_old.add_button('Изменить запрос', color=VkKeyboardColor.PRIMARY)

        self.keyboard_request = VkKeyboard(one_time=False)
        self.keyboard_request.add_button('Изменить возраст', color=VkKeyboardColor.SECONDARY)
        self.keyboard_request.add_button('Изменить пол', color=VkKeyboardColor.SECONDARY)
        self.keyboard_request.add_line()
        self.keyboard_request.add_button('Изменить город', color=VkKeyboardColor.SECONDARY)
        self.keyboard_request.add_button('Изменить положение', color=VkKeyboardColor.SECONDARY)
        self.keyboard_request.add_line()
        self.keyboard_request.add_button('Всё верно', color=VkKeyboardColor.PRIMARY)
        self.keyboard_request.add_line()
        self.keyboard_request.add_button('Удалить всё об о мне', color=VkKeyboardColor.NEGATIVE)

        self.keyboard_sex = VkKeyboard(one_time=True)
        self.keyboard_sex.add_button('Мужской', color=VkKeyboardColor.SECONDARY)
        self.keyboard_sex.add_button('Женский', color=VkKeyboardColor.SECONDARY)

        self.keyboard_marital_normal = VkKeyboard(one_time=False)
        self.keyboard_marital_normal.add_button('не женат (не замужем)', color=VkKeyboardColor.SECONDARY)
        self.keyboard_marital_normal.add_button('всё сложно', color=VkKeyboardColor.SECONDARY)
        self.keyboard_marital_normal.add_line()
        self.keyboard_marital_normal.add_button('в активном поиске', color=VkKeyboardColor.SECONDARY)
        self.keyboard_marital_normal.add_button('в гражданском браке', color=VkKeyboardColor.SECONDARY)


        self.keyboard_wrong = VkKeyboard(one_time=True)
        self.keyboard_wrong.add_button('Закончить', color=VkKeyboardColor.NEGATIVE)

        self.keyboard_new.get_keyboard()

    def send_msg(self, message: str, user_id: str, keyboard=None):
        self.vk_session.get_api().messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard=keyboard,
            message=message
        )

    def listen_dialog(self) -> list:
        lslongpooll = VkLongPoll(self.vk_session)

        for event in lslongpooll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                user_info = self.vk_session.get_api().users.get(
                    user_ids=event.user_id,
                    fields='sex,city,'
                )
                print(f'{event.user_id}: {event.text}')
                response = [user_info, event]
                return response

    def not_understand_msg(self, user_id: str):
        self.send_msg(message=f'Прости, я тебя не понимаю, давай попробуем начать все сначала',
                      user_id=user_id,
                      keyboard=self.keyboard_new.get_keyboard()
                      )

    def wrong_input(self, user_id):
        self.send_msg(message=f'Кажется, что-то пошло не так\n'
                              f'Может попробуешь снова',
                      user_id=user_id,
                      keyboard=self.keyboard_sex.get_keyboard()
                      )

    def new_user_search(self, user_id) -> dict:
        marital_status = int
        next_msg = True
        sex = int
        marital_status_dict = {
            'не женат (не замужем)': 1,
            'встречается':2,
            'помолвлен(-а)': 3,
            'женат (замужем)': 4,
            'всё сложно': 5,
            'в активном поиске': 6,
            'влюблен(-а)': 7,
            'в гражданском браке': 8
        }

        self.send_msg(message=f'Для начала на клавиатуре ниже выбери пол своей будущей второй половинке',
                      user_id=user_id,
                      keyboard=self.keyboard_sex.get_keyboard()
                      )
        text = self.listen_dialog()[1].txte
        if text == 'Мужской':
            sex = 2
        elif text == 'Женский':
            sex = 1
        else:
            self.not_understand_msg(user_id)

        self.send_msg(message=f'Отлично! Продолжаем. \n'
                              f'Напиши через пробел возростной интервал.',
                      user_id=user_id,
                      )
        while True:
            text = self.listen_dialog()[1].txte
            if text == 'Закончить':
                self.send_msg(message=f'Ииии... Закончали!',
                              user_id=user_id,
                              keyboard=self.keyboard_sex.get_keyboard()
                              )

                return None
            age = text.split()
            try:
                if int(age[0]) and int(age[1]):
                    break
            except ValueError:
                self.wrong_input(user_id)

        self.send_msg(message=f'Пришло время выбрать город.\n'
                              f'Какой город ты выберешь ?',
                      user_id=user_id,
                      )
        city = self.listen_dialog()[1].txte

        self.send_msg(message=f'Остался последний пункт надеюсь ты к нему готов.\n'
                              f'Выбери семейное положение.\n'
                              f'Хорошенько подумай прежде чем решить, тут ты не можешь ошибиться.\n'
                              f'Выберишь однажды не сможешь изменить никогда!!!👻',
                      user_id=user_id,
                      )
        self.send_msg(message=f'Шучу, ты всегда сможешь изменить настройки поиска😜',
                      user_id=user_id,
                      keyboard=self.keyboard_marital_normal.get_keyboard()
                      )
        text = self.listen_dialog()[1].txte

        search_dict = {
            'sex': sex,
            'age': age,
            'city': city,
            'marital_status': marital_status_dict[text]
        }

        return search_dict


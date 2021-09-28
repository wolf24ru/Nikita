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


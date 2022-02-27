import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType

import random

from parsing import news_events

token = "f64dac7a2454d26a07f4a7081417fa6ba1ffd3cc4b3d13b83162f353c3dd780c752d5c342e3555e8790fe"

main_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "О ТУСУР"
            },
            "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Учеба"
                },
                "color": "primary"
            }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Университетская жизнь"
            },
            "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": "Карьера"
                },
                "color": "primary"
            }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Справка"
            },
            "color": "secondary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"6\"}",
                    "label": "Контакты"
                },
                "color": "secondary"
            }]
    ]
}

main_keyboard = json.dumps(main_keyboard, ensure_ascii=False).encode('utf-8')
main_keyboard = str(main_keyboard.decode('utf-8'))

info_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Библиотеки"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Столовые"
            },
            "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Деканаты"
                },
                "color": "primary"
            }]
    ]
}

info_keyboard = json.dumps(info_keyboard, ensure_ascii=False).encode('utf-8')
info_keyboard = str(info_keyboard.decode('utf-8'))

learn_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Успеваемость",
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Расписание"
            },
            "color": "primary"
        }]
    ]
}

learn_keyboard = json.dumps(learn_keyboard, ensure_ascii=False).encode('utf-8')
learn_keyboard = str(learn_keyboard.decode('utf-8'))

life_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Новости"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Мероприятия"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Клубы по интересам"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Возможности"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Спорт"
            },
            "color": "primary"
        }]
    ]
}

life_keyboard = json.dumps(life_keyboard, ensure_ascii=False).encode('utf-8')
life_keyboard = str(life_keyboard.decode('utf-8'))

contacts_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"1\"}",
                "label": "Жене",
                "link": "https://vk.com/genemane"
            }
        },
            {
                "action": {
                    "type": "open_link",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Кате",
                    "link": "https://vk.com/astro_rin"
                }
            }],
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"3\"}",
                "label": "Роме",
                "link": "https://vk.com/id216917888"
            }
        },
            {
                "action": {
                    "type": "open_link",
                    "payload": "{\"button\": \"4\"}",
                    "label": "Вике",
                    "link": "https://vk.com/viki_foxxx"
                }
            }],

    ]
}

contacts_keyboard = json.dumps(contacts_keyboard, ensure_ascii=False).encode('utf-8')
contacts_keyboard = str(contacts_keyboard.decode('utf-8'))


def send(user_id, message, key=None):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'keyboard': key,
               'random_id': random.randint(0, 213144)})


vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

try:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if event.text.lower() == "о тусур":
                    send(event.user_id, "Немного о нашем университете:", info_keyboard)
                elif event.text.lower() == "учеба":
                    send(event.user_id, "Вот, что могу показать:", learn_keyboard)
                elif event.text.lower() == "университетская жизнь":
                    send(event.user_id, "О чём ты хочешь узнать?", life_keyboard)
                elif event.text.lower() == "контакты":
                    send(event.user_id, "По любым вопросам можешь обращаться к:", contacts_keyboard)
                elif event.text.lower() == "библиотеки":
                    send(event.user_id, "Наши библиотеки:")
                elif event.text.lower() == "столовые":
                    send(event.user_id, "Наши столовые:")
                elif event.text.lower() == "деканаты":
                    send(event.user_id, "Выберите факультет:")
                elif event.text.lower() == "успеваемость":
                    send(event.user_id, "Здесь вы можете узнать вашу успеваемость:\n www.ocenka.tusur.ru")
                elif event.text.lower() == "расписание":
                    send(event.user_id, "Введите группу или преподавателя:")
                elif event.text.lower() == "новости":
                    send(event.user_id, news_events("news"))
                elif event.text.lower() == "мероприятия":
                    send(event.user_id, news_events("events"))
                elif event.text.lower() == "клубы по интересам":
                    send(event.user_id, "*тут про клубы*")
                elif event.text.lower() == "возможности":
                    send(event.user_id, "*тут о возможностях*")
                elif event.text.lower() == "спорт":
                    send(event.user_id, "*тут о спорте*")
                elif event.text.lower() == "карьера":
                    send(event.user_id, "*тут о карьере*")
                elif event.text.lower() == "справка":
                    send(event.user_id,
                         "Я - бот из ТУСУР - Томского государственного университета систем управления и "
                         "радиоэлектроники. Меня создали студенты факультета вычислительных систем, чтобы собрать всю "
                         "самую основную, необходимую информацию для студента.\n "
                         "Что я могу рассказать:\n"
                         "1) Расположение и время работы корпусов библиотеки, столовых вуза, деканатов\n"
                         "Начало->Главное меню->О ТУСУР\n"
                         "2) Расписание занятий (можно подписаться на ежедневную отправку расписания), успеваемость\n"
                         "Начало->Главное меню->Учёба\n"
                         "3) Новости, мероприятия, клубы, возможности, спорт\n"
                         "Начало->Главное меню->Университетская жизнь\n"
                         "4) Карьера\n"
                         "Начало->Главное меню->Карьера)\n")
                else:
                    send(event.user_id, "Не понимаю тебя :(", main_keyboard)

except Exception as e:
    print(e)

from datetime import datetime

import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType

import random

from parsing import news_events, timetable

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
                "label": "Спорт"
            },
            "color": "primary"
        }]
    ]
}

life_keyboard = json.dumps(life_keyboard, ensure_ascii=False).encode('utf-8')
life_keyboard = str(life_keyboard.decode('utf-8'))

schedule_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "По группе"
            }
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "По преподавателю"
                }
            }],
    ]
}

schedule_keyboard = json.dumps(schedule_keyboard, ensure_ascii=False).encode('utf-8')
schedule_keyboard = str(schedule_keyboard.decode('utf-8'))

faculties_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "РТФ"
            },
            "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "РКФ"
                },
            "color": "primary"
            }
        ,{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "ФВС"
                },
            "color": "primary"
            }]
        ,[{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "ФСУ"
            },
            "color": "primary"
        }
        ,{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "ФЭТ"
            },
            "color": "primary"
        }
        ,{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"6\"}",
                "label": "ФИТ"
            },
            "color": "primary"
        }]
        ,[{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"7\"}",
                "label": "ЭФ"
            },
            "color": "primary"
        }
        ,{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"8\"}",
                "label": "ГФ"
            },
            "color": "primary"
        }
        ,{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"9\"}",
                "label": "ЮФ"
            },
            "color": "primary"
        }]
        ,[{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"10\"}",
                "label": "ФБ"
            },
            "color": "primary"
        }]
    ]
}

faculties_keyboard_1 = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "ЗиВФ"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "ФДО"
            },
            "color": "primary"
        }]
    ]
}

faculties_keyboard = json.dumps(faculties_keyboard, ensure_ascii=False).encode('utf-8')
faculties_keyboard = str(faculties_keyboard.decode('utf-8'))
faculties_keyboard_1 = json.dumps(faculties_keyboard_1, ensure_ascii=False).encode('utf-8')
faculties_keyboard_1 = str(faculties_keyboard_1.decode('utf-8'))

def send(user_id, message, key=None):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'keyboard': key,
               'random_id': random.randint(0, 213144)})


vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

stage = 0
search = ''
nowdate = datetime.now().strftime("%d.%m.%Y")
fac_f = open("adresses and shedules/faculties.txt", "r", encoding="utf-8")
fac_all = fac_f.readlines()

try:
    for event in longpoll.listen():
        sender = 1
        if event.type == VkEventType.MESSAGE_NEW and stage == 1:
            if event.to_me:
                search = event.text
                if not search.isalpha() and (search.lower != "по преподавателю" or search.lower != "по группе"):
                    send(event.user_id, "Ищу расписание группы "+search+"... ")
                    send(event.user_id, "Вот, что мне удалось найти: \n" + timetable(search, nowdate) + "\n\n Ищем что-то ещё?", schedule_keyboard)
                    stage = 0
                    sender = 0
                elif search.isalpha() and (search.lower != "по преподавателю" or search.lower != "по группе"):
                    send(event.user_id, "Ищу расписание преподавателя "+search+"... ")
                    send(event.user_id, "Вот, что мне удалось найти: \n" + timetable(search, nowdate) + "\n\n Ищем что-то ещё?", schedule_keyboard)
                    stage = 0
                    sender = 0
        if event.type == VkEventType.MESSAGE_NEW and stage == 0:
            if event.to_me:
                if event.text.lower() == "о тусур":
                    send(event.user_id, "Немного о нашем университете:", info_keyboard)
                elif event.text.lower() == "учеба":
                    send(event.user_id, "Вот, что могу показать:", learn_keyboard)
                elif event.text.lower() == "университетская жизнь":
                    send(event.user_id, "О чём ты хочешь узнать?", life_keyboard)
                elif event.text.lower() == "столовые":
                    send(event.user_id, "Столовые ТУСУР\n"
                                        "пн – сб с 09:00 до 18:00\n"
                                        "Главный корпус, ФЭТ, РК, УЛК")
                elif event.text.lower() == "библиотеки":
                    send(event.user_id, "Библиотеки ТУСУР\n"
                                        "Пн. – пт.: 9:00 – 18:00\n"
                                        "Перерыв с 13:15 до 13:45\n"
                                        "Cб., вс.: выходные дни\n"
                                        "ул. Красноармейская, 146 (УЛК))\n"
                                        "На карте: https://www.google.com/maps/place/ТУСУР+Учебно-лабораторный+Корпус/@56.4540991,84.9758276,17z/data=!3m1!4b1!4m5!3m4!1s0x4326ecae4a242255:0xedadec8893875cac!8m2!3d56.4540991!4d84.9780163")
                elif event.text.lower() == "деканаты":
                    send(event.user_id, "Выберите факультет: ", faculties_keyboard)
                    send(event.user_id, "Так же заочный и дистанционный: ",faculties_keyboard_1)
                elif event.text.lower() == "успеваемость":
                    send(event.user_id, "Здесь вы можете узнать вашу успеваемость:\n www.ocenka.tusur.ru")
                elif event.text.lower() == "расписание":
                    send(event.user_id, "Что ищем?", schedule_keyboard)
                elif event.text.lower() == "по группе":
                    send(event.user_id, "Хорошо, напиши мне номер группы")
                    stage = 1
                elif event.text.lower() == "по преподавателю":
                    send(event.user_id, "Всё могу, только назови преподавателя\n Мне достаточно фамилии, но для точности результата мне лучше знать полные инициалы\n Чьё расписание ищем?")
                    stage = 1
                elif event.text.lower() == "новости":
                    send(event.user_id, news_events("news"))
                elif event.text.lower() == "мероприятия":
                    send(event.user_id, news_events("events"))
                elif event.text.lower() == "клубы по интересам":
                    send(event.user_id, "Вся информация по клубам: \nhttps://tusur.ru/ru/studentam/kluby-po-interesam-i-volonterstvo")
                elif event.text.lower() == "спорт":
                    send(event.user_id, news_events("sport"))
                elif event.text.lower() == "карьера":
                    send(event.user_id, news_events("cstv"))
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
                #Далее факультеты
                elif event.text.lower() == "ртф":
                    fac_current = 0
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "ркф":
                    fac_current = 8
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "фвс":
                    fac_current = 16
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "фсу":
                    fac_current = 23
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "фэт":
                    fac_current = 30
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "фит":
                    fac_current = 38
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "эф":
                    fac_current = 45
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "гф":
                    fac_current = 53
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "юф":
                    fac_current = 60
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "фб":
                    fac_current = 67
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "зивф":
                    fac_current = 75
                    fac_msg = ""
                    for x in range(fac_current, fac_current+7):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif event.text.lower() == "фдо":
                    fac_current = 82
                    fac_msg = ""
                    for x in range(fac_current, fac_current+6):
                        fac_msg = fac_msg + "".join(fac_all[x])
                    send(event.user_id, fac_msg)
                elif sender:
                    send(event.user_id, "Я тебя не понял :(\n Уточни команду!", main_keyboard)
                    sender = 0

except Exception as e:
    print(e)
                #Доделать инфу, факультеты для деканатов

import vk_api, json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time
import random
from bs4 import BeautifulSoup

token = "f64dac7a2454d26a07f4a7081417fa6ba1ffd3cc4b3d13b83162f353c3dd780c752d5c342e3555e8790fe"
vk = vk_api.VkApi(token=token)
vk._auth_token()

def send(id, message, keyboard = None):
    msg_options = {
        "user_id": id,
        "message": message,
        "random_id": random.randint(1, 2147483647)
    }
    if keyboard != None:
        msg_options["keyboard"] = keyboard.get_keyboard()
    else:
        msg_options = msg_options

    vk.method("messages.send", msg_options)

def create_keys(btns):
    nb = []
    color = ''
    for i in range(len(btns)):
        nb.append([])
        for k in range(len(btns[i])):
            nb[i].append(None)
    for i in range(len(btns)):
        for k in range(len(btns[i])):
            caption = btns[i][k][0]
            color = {'зеленый': 'POSITIVE', 'красный': 'NEGATIVE', 'синий': 'PRIMARY', 'белый': 'SECONDARY'}[btns[i][k][1]]
            nb[i][k] = {"action": {"type": "text", "label": f"{caption}"}, "color": f"{color}"}
    new_keys = {'one_time': False, 'buttons': nb}
    new_keys = json.dumps(new_keys, ensure_ascii=False).encode('utf-8')
    new_keys = str(new_keys.decode('utf-8'))
    return new_keys

begin_keys = create_keys([
    [('Начать', 'синий'), ('Справка', 'белый')]
])
main_menu_keys = create_keys([
    [('О ТУСУР', 'синий'), ('Учеба', 'синий'), ('Университетская жизнь', 'синий'), ('Карьера', 'синий')]
])
info_keys = create_keys([
    [('Библиотеки', 'синий'), ('Столовые', 'синий'), ('Деканаты', 'синий'), ('Назад', 'белый')]
])
decks_keys = create_keys([
    [('Открыть список факультетов', 'синий'), ('Назад', 'белый')]
])
learn_keys = create_keys([
    [('Открыть мою успеваемость', 'синий'), ('Открыть моё расписание', 'синий'), ('Назад', 'белый')]
])
life_keys = create_keys([
    [('Новости', 'синий'), ('Мероприятия', 'синий'), ('Клубы', 'синий'), ('Возможности', 'синий'), ('Спорт', 'синий'), ('Назад', 'белый')]
])

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 150, "filter": "unanswered"})
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if messages["count"] >= 1:
            if body.lower() == "привет" or body.lower() == "начать" or body.lower() == "хай" or body.lower() == "ку":
                send(id, "Привет! Вот с чем я могу тебе помочь:", main_menu_keys)
            if body == "О ТУСУР":
                send(id, "Информация об университете:", info_keys)
            if body == "Учеба":
                send(id, "Всё о учёбе:", learn_keys)
            if body == "Университетская жизнь":
                send(id, "Всё о жизни в университете:", life_keys)
            if body == "Карьера":
                send(id, "https://cstv.tusur.ru")
            if body == "Справка":
                send(id, "Я - бот из ТУСУР - Томского государственного университета систем управления и радиоэлектроники.\n"
                         "Меня создали студенты факультета вычислительных систем, чтобы собрать всю самую основную, необходимую информацию для студента.\n"
                         "Что я могу рассказать:\n"
                         "1) Расположение и время работы корпусов библиотеки, столовых вуза, деканатов(Начало->Главное меню->О ТУСУР)\n"
                         "2) Расписание занятий (можно подписаться на ежедневную отправку расписания), успеваемость(Начало->Главное меню->Учёба)\n"
                         "3) Новости, мероприятия, клубы, возможности, спорт(Начало->Главное меню->Университетская жизнь)\n"
                         "4) О карьере(Начало->Главное меню->Карьера)\n"
                         "Для обратной связи обращайся в нашу группу ВКонтакте!")
    except Exception as E:
        time.sleep(0)

## https://www.youtube.com/watch?v=Vvih70FvRno

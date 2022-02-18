import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time
import random
from bs4 import BeautifulSoup

token = "f64dac7a2454d26a07f4a7081417fa6ba1ffd3cc4b3d13b83162f353c3dd780c752d5c342e3555e8790fe"
vk = vk_api.VkApi(token=token)
vk._auth_token()

def gen_link(count):
    arr = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h',
           'j','k','l','z','x','c','v','b','n','m']
    arr_n = ['1','2','3','4','5','6','7','8','9']
    passw = []
    for i in range(count):
        if i == count-1:
            passw.append(random.choice(arr_n))
        else:
            passw.append(random.choice(arr))
    return "".join(passw)

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
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 150, "filter": "unanswered"})
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if messages["count"] >= 1:
            if (body.lower() == "привет") or (body.lower() == "начать") or (body.lower() == "хай") or (body.lower() == "ку"):
                keyboard = VkKeyboard()
                keyboard.add_button("О ТУСУР", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Учеба", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Жизнь в университете", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Карьера", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Справка", VkKeyboardColor.SECONDARY)
                send(id, "Привет! Вот с чем я могу тебе помочь:", keyboard)
            if (body == "Справка"):
                send(id, "Бот создан с целью помочь студентам с поиском информации о университете.")
                ##vk.method("messages.send", {"peer_id": id, "message": "Такой команды я не знаю :(", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(0)

## https://www.youtube.com/watch?v=Vvih70FvRno

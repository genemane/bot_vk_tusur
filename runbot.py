import vk_api
import time
import random
from bs4 import BeautifulSoup
token = "f64dac7a2454d26a07f4a7081417fa6ba1ffd3cc4b3d13b83162f353c3dd780c752d5c342e3555e8790fe"
import random, time
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

vk = vk_api.VkApi(token=token)
vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if (body.lower() == "привет") or (body.lower() == "начать"):
                vk.method("messages.send", {"peer_id": id, "message": "Привет! Я могу дать тебе ссылки на случайный скриншот с сайта Lightshot'а.  Напиши <найди> или <еще> и проверь!", "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": "Некоторые ссылки могут не работать,так как скриншоты удаляются, иногда придется пробовать несколько раз.", "random_id": random.randint(1, 2147483647)})
            elif (body.lower() == "найди") or (body.lower() == "еще"):
                vk.method("messages.send", {"peer_id": id, "message": "www.prnt.sc/"+gen_link(int(6)), "dont_parse_links": 0, "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Такой команды я не знаю :(", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(0)

## https://www.youtube.com/watch?v=Vvih70FvRno

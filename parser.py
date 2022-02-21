import requests
from bs4 import BeautifulSoup

# Главная / Новости и мероприятия
url_main = 'https://tusur.ru/ru/novosti-i-meropriyatiya'

# Главная / Новости и мероприятия / Новости
url_news = 'https://tusur.ru/ru/novosti-i-meropriyatiya/novosti'

# Главная / Новости и мероприятия / Жизнь в ТУСУРе
url_tusur = 'https://tusur.ru/ru/novosti-i-meropriyatiya/jizn-v-tusure'

# Главная / Новости и мероприятия / Анонсы мероприятий
url_events = 'https://tusur.ru/ru/novosti-i-meropriyatiya/anonsy-meropriyatiy'

# Расписание
url_timetable = 'https://timetable.tusur.ru'


# Новости | Жизнь в ТУСУРе | Календарь мероприятий
# class_name - одно из значений "news relative", "life-in-tusur relative", "events relative"
def news_events(class_name):
    page = requests.get(url_main)
    final_message: str = ""
    # если запрос выполнен успешно, то код - 2xx
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        items = soup.find(class_=class_name).findAll(class_='news-item')
        news_item = []
        for item in items:
            if class_name == "events relative":
                news_item.append(item.find(class_='strong').get_text(" ", strip=True))
            else:
                news_item.append(item.find(class_='since').get_text(strip=True))
            news_item.append(item.find(class_='title').get_text(strip=True))
            if class_name == "news relative":
                news_item.append(item.find(class_='annotation hidden-lg').get_text(strip=True))
            else:
                news_item.append(" ")
            news_item.append(item.find('a').get('href'))
            final_message = final_message + f'({news_item[0]}) {news_item[1]}\n'
            if news_item[2] != " ":
                final_message = final_message + f'\t{news_item[2]}\n'
            final_message = final_message + f'https://tusur.ru{news_item[3]}\n\n'
            news_item.clear()
        final_message = final_message + f'Больше информации можно найти здесь: {url_main}'

    # нет доступа к указанному url
    else:
        final_message = 'К сожалению, в данный момент я не могу ничего показать. Проблемы на сайте('
    # вместо print - отправлять final_message собеседнику
    return final_message


def timetable(group, teacher, date):
    url_timetable = 'https://timetable.tusur.ru'
    params = None
    tables_news = requests.get(url_timetable, params=params)
    if tables_news.status_code == 200:
        soup = BeautifulSoup(tables_news.text, 'html.parser')
        items = soup.find_all('', class_='news-page-list-item')
        new = []
        for item in items:
            new.append(item.find())
            new.append(item.find())

        final_message = f'{new[0]}\n\n{new[1]}\nБольше новостей Вы можете найти на сайте: {url_timetable}'
        new.clear()
    # нет доступа к указанному url
    else:
        final_message = 'Извините, какие-то проблемы с расписанием.'
    print(final_message)

import requests
from bs4 import BeautifulSoup
import re

url_main = 'https://tusur.ru'  # Главная
url_cstv = 'https://cstv.tusur.ru'  # Карьера
url_sport = 'https://sport.tusur.ru'  # Спорт в ТУСУРе
url_timetable = 'https://timetable.tusur.ru'  # Расписание занятий
schedule = {
    '1-я пара': '08:50 – 10:25',
    '2-я пара': '10:40 – 12:15',
    '3-я пара': '13:15 – 14:50',
    '4-я пара': '15:00 – 16:35',
    '5-я пара': '16:45 – 18:20',
    '6-я пара': '18:30 – 20:05',
    '7-я пара': '20:15 – 21:50'
}


# Новости | Спорт в ТУСУРе | Карьера | Календарь мероприятий | Жизнь в ТУСУРе
# class_name - одно из значений 'news' новости, 'sport' спорт в ТУСУРе,
# 'cstv' карьера, 'events' мероприятия, 'life-in-tusur' жизнь в ТУСУРе
def news_events(class_name):
    url = url_main
    subclass_name = 'news-item'
    if class_name == 'sport':
        class_name = 'news'
        subclass_name = 'row'
        url = f'{url_sport}/ru/novosti-i-meropriyatiya/novosti'
    elif class_name == 'cstv':
        class_name = 'news relative'
        url = url_cstv
    else:
        class_name = f'{class_name} relative'
    page = requests.get(url)
    final_message = ''
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        items = soup.find(class_=class_name).findAll(class_=subclass_name, limit=5)
        url_tmp = url
        if url == url_main:
            url_tmp = url + soup.find(class_=class_name).find('a').get('href')
        elif class_name == 'news':
            url = url_sport
        news_item = []
        for item in items:
            if class_name == 'events relative':
                news_item.append(item.find(class_='strong').get_text(' ', strip=True))
            elif class_name == 'news':
                news_item.append(item.find(class_='date').get_text(strip=True))
            else:
                news_item.append(item.find(class_='since').get_text(strip=True))
            if class_name == 'news':
                news_item.append(item.find('h5').find('a').get_text(strip=True))
            else:
                news_item.append(item.find(class_='title').get_text(strip=True))
            news_item.append(item.find(class_=re.compile('annotation')))
            news_item.append(item.find('a').get('href'))
            final_message = f'{final_message}(📆 {news_item[0]}) {news_item[1]}\n'
            if news_item[2] is not None:
                news_item[2] = news_item[2].get_text(strip=True)
                final_message = f'{final_message}{news_item[2]}\n'
            final_message = f'{final_message}{url}{news_item[3]}\n\n'
            news_item.clear()
        final_message = f'{final_message}Больше информации можно найти здесь: {url_tmp}'
    else:
        final_message = 'К сожалению, в данный момент я не могу ничего показать. Проблемы на сайте('
    return final_message


# Расписание занятий группы/преподавателя
def timetable(search, date):
    url = requests.get(f'{url_timetable}/searches/common_search?utf8=✓&search%5Bcommon%5D={search}&commit=Найти').url \
          + '?week_id=602'
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        temp = soup.find(class_='col-md-12 search')
        if temp is None:
            timetables = soup.find(class_='timetable_wrapper')
            headline = timetables.find('h1').get_text(strip=True)
            week = timetables.find(class_=re.compile('tile swiper-slide current')).find('div').get_text(strip=True) \
                .replace(' ', '').replace('\n', ' ')
            final_message = f'{headline}, неделя - {week}'
            tables = timetables.findAll(class_='table table-bordered table-condensed visible-xs visible-sm table-lessons noprint even')
            lessons = []
            for item in tables:
                item_date = item.find(class_='modal-body')
                if item_date is not None:
                    item_date.find('p')
                    print(item_date)
                    # если нет расписания?
                    if item_date == date or date == 'all-week':
                        # print(item.get_text('\n', strip=True))
                        # new.append(item.find())
                        # new.append(item.find())
                        # final_message = f'{new[0]}\n\n{new[1]}\n'
                        lessons.clear()
                else:
                    final_message = f'{final_message}\n\n{date} - в этот день нет пар'
        else:
            final_message = 'Не могу найти расписание. Пожалуйста, уточните номер группы или фамилию и имя преподавателя'
    else:
        final_message = 'Извините, какие-то проблемы с расписанием. Попробуйте снова чуть позже'
    return final_message


# print(timetable('599-1', '07.03.2022'))

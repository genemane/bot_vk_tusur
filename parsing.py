import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

url_main = 'https://tusur.ru'  # Главная страница
url_cstv = 'https://cstv.tusur.ru'  # Карьера
url_sport = 'https://sport.tusur.ru'  # Спорт в ТУСУРе
url_timetable = 'https://timetable.tusur.ru'  # Расписание занятий
schedule = {
    '08:50 - 10:25': '1-я пара',
    '10:40 - 12:15': '2-я пара',
    '13:15 - 14:50': '3-я пара',
    '15:00 - 16:35': '4-я пара',
    '16:45 - 18:20': '5-я пара',
    '18:30 - 20:05': '6-я пара',
    '20:15 - 21:50': '7-я пара'
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
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Referer': 'https://www.google.com'
    }
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        items = soup.find(class_=class_name).find_all(class_=subclass_name, limit=5)
        url_tmp = url
        if url == url_main:
            url_tmp = url + soup.find(class_=class_name).find('a').get('href')
        elif class_name == 'news':
            url = url_sport
        final_message = ''
        news_item = []
        for item in items:
            news_item.append(item.find(attrs={'class': ['strong', 'date', 'since']}).get_text(' ', strip=True))
            if class_name == 'news':
                news_item.append(item.find('h5').find('a').get_text(strip=True))
            else:
                news_item.append(item.find(class_='title').get_text(strip=True))
            news_item.append(item.find(class_=re.compile('annotation')))
            news_item.append(item.find('a').get('href'))
            final_message += f'(📆 {news_item[0]}) {news_item[1]}\n'
            if news_item[2] is not None:
                final_message += f'{news_item[2].get_text(strip=True)}\n'
            final_message += f'Источник: {url}{news_item[3]}\n\n'
            news_item.clear()
        final_message += f'Больше информации можно найти здесь: {url_tmp}'
    except Exception as e:
        print(e)
        final_message = f'{soup.find(class_=class_name)}Код: {page.status_code}\n{e}\nК сожалению, в данный момент я не могу это показать. Попробуй снова чуть позже'
    return final_message


# Расписание занятий группы/преподавателя
def timetable(search):
    try:
        url = requests.get(f'{url_timetable}/searches/common_search?utf8=✓&search%5Bcommon%5D={search}&commit=Найти').url
        page = requests.get(url, headers={'User-Agent': UserAgent().chrome})
        soup = BeautifulSoup(page.text, 'html.parser')
        if soup.find(class_='col-md-12 search') is None:
            timetables = soup.find(class_='timetable_wrapper')
            headline = timetables.find('h1').get_text(strip=True)
            week = timetables.find(class_=re.compile('tile swiper-slide current')).find('div').get_text(strip=True) \
                .replace(' ', '').replace('\n', ' ')
            final_message = f'{headline}, неделя - {week}'
            empty_week = soup.find(class_='margin-top-25 margin-bottom-25 text-danger')
            if empty_week is None:
                tables = timetables.find_all(class_=re.compile('table table-bordered table-condensed visible-xs'))
                for item in tables:
                    empty_day = item.find(class_='modal-body')
                    day = item.find('th').find_next('th').get_text(strip=True).replace('  ', '').replace('\n', ' ')
                    final_message += f'\n\n📆 {day}\n'
                    if empty_day is not None:
                        lessons = item.find_all(class_=re.compile('lesson_\\d'))
                        for lesson in lessons:
                            info = lesson.find(class_='hidden for_print')
                            if info is not None:
                                time = lesson.find('span')
                                temp = time.get_text(strip=True)
                                time = f"{temp} - {time.find_next('span').get_text(strip=True)}"
                                time = f'{schedule[time]}, {time}'
                                discipline = info.find(class_='discipline').get_text(strip=True)
                                kind = info.find(class_='kind').get_text(strip=True)
                                group = info.find(class_='group').get_text(strip=True)
                                aud = info.find(class_='auditoriums').get_text(strip=True)
                                note = info.find(class_='note')
                                final_message += f'\n⏳ {time}\n📚 {discipline} {kind}\n'
                                if group != '':
                                    final_message += f'👤 {group}\n'
                                if aud != '':
                                    final_message += f'🚪 {aud}\n'
                                if note is not None:
                                    final_message += f'💬 {note.get_text(strip=True)}\n'
                    else:
                        final_message += ' - в этот день нет занятий'
            else:
                final_message += f'\n\n{empty_week.get_text(strip=True)}'
        else:
            final_message = 'Не могу найти расписание. Пожалуйста, уточни номер группы или фамилию и имя преподавателя'
    except Exception as e:
        print(e)
        final_message = 'Извини, какие-то проблемы с расписанием. Попробуй снова чуть позже'
    return final_message

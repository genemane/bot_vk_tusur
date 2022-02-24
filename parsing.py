import requests
from bs4 import BeautifulSoup

url_main = 'https://tusur.ru'  # Главная
url_timetable = 'https://timetable.tusur.ru'  # Расписание
url_grades = 'https://ocenka.tusur.ru'  # Успеваемость обучающегося


# Новости | Жизнь в ТУСУРе | Календарь мероприятий
# class_name - одно из значений 'news', 'life-in-tusur', 'events'
def news_events(class_name):
    page = requests.get(url_main)
    final_message = ''
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        class_name = class_name + ' relative'
        items = soup.find(class_=class_name).findAll(class_='news-item')
        url = url_main + soup.find(class_=class_name).find('a').get('href')
        news_item = []
        for item in items:
            if class_name == 'events relative':
                news_item.append(item.find(class_='strong').get_text(" ", strip=True))
            else:
                news_item.append(item.find(class_='since').get_text(strip=True))
            news_item.append(item.find(class_='title').get_text(strip=True))
            if class_name == 'news relative':
                news_item.append(item.find(class_='annotation hidden-lg').get_text(strip=True))
            else:
                news_item.append(' ')
            news_item.append(item.find('a').get('href'))
            final_message = final_message + f'({news_item[0]}) {news_item[1]}\n'
            if news_item[2] != ' ':
                final_message = final_message + f'\t{news_item[2]}\n'
            final_message = final_message + f'{url_main}{news_item[3]}\n\n'
            news_item.clear()
        final_message = final_message + f'Больше информации можно найти здесь: {url}'
    else:
        final_message = 'К сожалению, в данный момент я не могу ничего показать. Проблемы на сайте('
    return final_message


# Получение URL-адреса страницы с расписанием группы или преподавателя в заданный промежуток времени
def get_url(item, date):
    url = requests.get(f'{url_timetable}/searches/common_search?utf8=✓&search%5Bcommon%5D={item}&commit=Найти').url
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')

        current_week = soup.find
        week = 0
    # добавить к url номер недели, если дата не попадает на текущую неделю
    url = url + f'?week_id={week}'
    return url


# group, teacher, date
# Расписание группы
def timetable(group, date):
    url = requests.get(f'{url_timetable}/searches/common_search?utf8=✓&search%5Bcommon%5D={group}&commit=Найти').url \
          + '?week_id=602'
    page = requests.get(url)
    final_message = ''
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        # обработка исключений AttributeError
        temp = soup.find(class_='col-md-12 search')
        if temp is not None:
            final_message = f"{temp.find('h1').get_text(strip=True)}. Не могу найти расписание. " \
                            f"Пожалуйста, уточните номер группы"
        else:
            # headline = soup.find(class_='col-md-12').find('h1').get_text(strip=True)
            # week = soup.find(class_='tile swiper-slide current day_color_theoretical swiper-slide-next').\
                # find('a').get_text(strip=True)
            tables = soup.findAll('tbody')  # .get_text('\n', strip=True)
            new = []
            for item in tables:
                print(item.get_text('\n', strip=True))
                # new.append(item.find())
                # new.append(item.find())
                # final_message = f'{new[0]}\n\n{new[1]}\n'
                new.clear()

    else:
        final_message = 'Извините, какие-то проблемы с расписанием. Попробуйте снова чуть позже'
    return final_message


# class_name - одно из значений 'news', 'life-in-tusur', 'events'
# print(news_events('news'))
# print(timetable('599-1', '07.03.2022'))

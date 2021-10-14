from datetime import date
import datetime
import json

def user_chat():
    try:
        new_line = '\n'
        period = int(input(f'За какой период нужны данные? {new_line} 1 - один день, {new_line} 2 - последняя неделя, {new_line} 3 - месяц, {new_line} 4 - полгода, {new_line} другое число - все время работы системы мониторинга трафика {new_line}'))
        if period == 1:
            print('Выбрана аналитика за вчерашний день')
        elif period == 2:
            print('Выбрана аналитика за прошедшую неделю')
        elif period == 3:
            print('Выбрана аналитика за последние полгода')
        elif period == 4:
            print('Выбрана аналитика за последний год')
        else:
            print('Выбрана аналитика за весь период обслуживания')
    except TypeError:
        period = 4
        print('Выбрана аналитика за последний год')

    def find_day():
        today = date.today()
        yesterday = today - datetime.timedelta(days=30)
        return yesterday

today = date.today()
yesterday = find_day()
file_title = str(f'{yesterday}_{today}')


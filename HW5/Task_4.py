#Выведите дату в следующем формате
#Имя_дня  Имя_дня  Имя_месяца  года

from datetime import datetime

given_date = datetime(2020, 2, 25)

days = {
    0: 'понедельник', 1: 'вторник', 2: 'среда',
    3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'
}

months = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
    5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
    9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
}

day_name = days[given_date.weekday()]
month_name = months[given_date.month]
found_date = f'{day_name.capitalize()}, {given_date.day} {month_name} {given_date.year} г.'

print(found_date)



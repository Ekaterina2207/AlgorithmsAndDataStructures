#Найдите день недели для заданной даты

from datetime import datetime

given_date = datetime(2020, 7, 26)

days = {
    0: 'понедельник', 1: 'вторник', 2: 'среда',
    3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'
}

day_name = days[given_date.weekday()]
print(day_name.capitalize())

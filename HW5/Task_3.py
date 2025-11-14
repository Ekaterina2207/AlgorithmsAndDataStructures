#Вычтите неделю (7 дней) из заданной даты

from datetime import datetime, timedelta

iven_date = datetime(2020, 2, 25)
found_date = iven_date - timedelta(days=7)
print(found_date.strftime("%Y-%m-%d"))

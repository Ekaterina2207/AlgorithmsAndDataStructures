#Прибавьте к заданной дате неделю (7 дней) и 12 часов

from datetime import datetime, timedelta
given_date = datetime(2020, 3, 22, 10, 0, 0)
found_date = given_date + timedelta(days=7, hours=12)
print(found_date)
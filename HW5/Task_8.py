#Преобразуйте следующее datetime в строку

from datetime import datetime

given_date = datetime(2020, 2, 25)
print(given_date.strftime("%Y-%m-%d %H:%M:%S"))
#Вычислите количество дней между двумя заданными датами

from datetime import datetime

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

delta = date_2 - date_1

print(f'{delta.days} дней')
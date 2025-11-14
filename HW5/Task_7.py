#Выведите текущее время в миллисекундах

from datetime import datetime

current_datetime = datetime.now()
current_time = current_datetime.time()
print(current_time)
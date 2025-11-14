#Преобразование строки в объект datetime

import datetime

date_string = "Feb 25 2020 4:20PM"
datetime_obj = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(datetime_obj)
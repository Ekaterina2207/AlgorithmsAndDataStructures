from utils import open_json
my_filename = input('Введите имя файла: ')
month_temps = open_json(my_filename)
if month_temps:
    temp_by_day = {}
    for day_num, day_temp in enumerate(month_temps['temps']):
        temp_by_day[f"{day_num + 1:02}-{month_temps['month']:02}-{month_temps['year']}"] = day_temp
    print(temp_by_day)
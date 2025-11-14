#Фильтрация данных
#Выбрать строки, где продажи больше 1000
#Найти записи за определенный период
#Отфильтровать по нескольким условиям

import pandas as pd
import numpy as np

sales = pd.read_csv('sales.csv', parse_dates=['date'])
sales1000 = sales[sales['sales'] >= 1000]
first_date = '2023-01-01'
last_date = '2023-02-28'
period = sales[(sales['date'] >= first_date) & (sales['date'] <= last_date)]
print(sales1000)
print(period)
city_category = sales[(sales['city'] == 'Москва') & (sales['category'] == 'Одежда')]
print(city_category)


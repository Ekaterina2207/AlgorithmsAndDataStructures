#Чтение и первичная обработка
#Загрузить CSV файл sales.csv
#Вывести первые 5 строк
#Проверить наличие пропущенных значений
#Получить основную статистику по числовым столбцам


import pandas as pd

sales = pd.read_csv('sales.csv')
five_string = sales.head()
none = sales.isna().sum()
statistic = sales.describe()
print(five_string)
print()
print(none)
print()
print(statistic)

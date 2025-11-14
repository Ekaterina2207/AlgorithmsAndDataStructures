#Работа с NaN
#Заполнить пропуски средним значением
#Удалить строки с пропущенными данными
#Создать новый столбец на основе существующих

import pandas as pd

sale = pd.read_csv('sales.csv')
print(sale.isna().sum())
sale['quantity'] = sale['quantity'].fillna(sale['quantity'].mean())
#Считаем корректную сумму продаж (sales), т.к. при создании csv-файла, sales считала как qty*price
mask = sale['sales'].isna()
sale.loc[mask, 'sales'] = sale.loc[mask, 'quantity'] * sale.loc[mask, 'price']
print(sale)
sale = sale.dropna() #удаляем строки с пропущенными городами
sale['cheap_or_expensive'] = sale['price'].apply(lambda x: 'Дорогой' if x > 2000 else 'Дешёвый')
print(sale)
print(sale.isna().sum())


#Группировка данных
#Посчитать суммарные продажи по городам
#Найти средний чек по категориям товаров
#Определить топ-5 по объему покупок

import pandas as pd

df = pd.read_csv('sales.csv')
sum_city = df.groupby('city')['sales'].sum()
avg_cat = df.groupby('category')['sales'].mean()
top_5 = df.sort_values('sales', ascending=False)[:5]
print(sum_city)
print(avg_cat)
print(top_5)


#print(new_list1['broadband'].agg(['mean']))
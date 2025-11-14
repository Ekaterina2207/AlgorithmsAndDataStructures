#Топ 100 популярных имен за период с 2015 по 2025 год (график)
#Топ 10 популярных мужских имен за каждый месяц (график или графики)
#Топ 10 популярных женских имен за каждый месяц (график или графики)
#Топ 10 популярных мужских имен за весь период (график или графики)
#Топ 10 популярных женских имен за весь период (график или графики)

import matplotlib.pyplot as plt
import pandas as pd
import csv

df_men_names = pd.read_csv('Number_of_names_man.csv', sep=';', skiprows=1)
df_women_names = pd.read_csv('Number_of_names_woman.csv', sep=';', skiprows=1)

df_women_names.columns = df_men_names.columns

df_mixed_names = pd.concat([df_men_names, df_women_names], ignore_index=True)

#Топ 100 популярных имен за период с 2015 по 2025 год

top_100 = (df_mixed_names
           .groupby('Имя')['Количество человек']
           .sum()
           .reset_index()
           .sort_values('Количество человек', ascending=False)
           .head(100))

plt.figure(figsize=(8, 30))
plt.barh(top_100['Имя'], top_100['Количество человек'])
plt.title('ТОП-100 имен 2015-2025')
plt.gca().invert_yaxis()
plt.yticks(fontsize=5)
plt.show()

#Топ 10 популярных мужских имен за каждый месяц

months_men_10 = df_men_names[df_men_names['Год'] == 2023]
for month in months_men_10['Месяц'].unique():
    month_data = months_men_10[months_men_10['Месяц'] == month]
    result = (month_data.groupby('Имя')['Количество человек']
              .sum()
              .reset_index()
              .sort_values('Количество человек', ascending=False)
              .head(10))
    plt.figure(figsize=(8, 10))
    plt.barh(result['Имя'], result['Количество человек'])
    plt.title(f'ТОП-10 мижских имен {month} 2023')
    plt.gca().invert_yaxis()
    plt.show()


#Топ 10 популярных женских имен за каждый месяц

months_women_10 = df_women_names[df_women_names['Год'] == 2023]
for month in months_women_10['Месяц'].unique():
    month_data = months_women_10[months_women_10['Месяц'] == month]
    result = (month_data.groupby('Имя')['Количество человек']
              .sum()
              .reset_index()
              .sort_values('Количество человек', ascending=False)
              .head(10))
    plt.figure(figsize=(8, 10))
    plt.barh(result['Имя'], result['Количество человек'])
    plt.title(f'ТОП-10 женских имен {month} 2023')
    plt.gca().invert_yaxis()
    plt.show()


#Топ 10 популярных мужских имен за весь период

top_10_men = (df_men_names
                 .groupby('Имя')['Количество человек']
                 .sum()
                 .reset_index()
                 .sort_values('Количество человек', ascending=False)
                 .head(10))

plt.figure(figsize=(8, 15))
plt.barh(top_10_men['Имя'], top_10_men['Количество человек'])
plt.title('ТОП-10 популярных мужских имен 2015-2025')
plt.gca().invert_yaxis()
plt.yticks(fontsize=8)
plt.show()

#Топ 10 популярных женских имен за весь период

top_10_women = (df_women_names
                 .groupby('Имя')['Количество человек']
                 .sum()
                 .reset_index()
                 .sort_values('Количество человек', ascending=False)
                 .head(10))

plt.figure(figsize=(8, 15))
plt.barh(top_10_women['Имя'], top_10_women['Количество человек'])
plt.title('ТОП-10 популярных женских имен 2015-2025')
plt.gca().invert_yaxis()
plt.yticks(fontsize=8)
plt.show()
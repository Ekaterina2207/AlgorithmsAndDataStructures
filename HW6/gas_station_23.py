from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
import json
from datetime import datetime

df_zap_33 = pd.read_csv('zap_data_33.csv')
df_calib = pd.read_csv('calib.csv')

df_zap_33['data'] = df_zap_33['can_data'].apply(lambda x: json.loads(x))
df_zap_33['LLS'] = df_zap_33['data'].apply(lambda x: x.get('LLS_0'))
df_zap_33.drop(columns=['data'], inplace=True)
df_zap_33.drop(columns=['can_data'], inplace=True)

df_zap_33 = df_zap_33.dropna()

print(df_zap_33.head())

df_zap_33['datetime'] = pd.to_datetime(df_zap_33['timestamp'], unit='s')
df_zap_33['month'] = df_zap_33['datetime'].dt.month
month_names = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
    5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
    9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

print(df_zap_33.head())

for month in range(1,13):
    data = df_zap_33[df_zap_33['month'] == month]
    plt.figure(figsize=(12, 5))
    plt.plot(data['datetime'], data['speed'])
    plt.title(f'График скорости от времени, {month_names[month]}')
    plt.xlabel('Время')
    plt.ylabel('Скорость')
    plt.show()



import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
from datetime import datetime
from geopy.distance import geodesic


df_gps = pd.read_csv('data_03.csv')
df_gps = df_gps.dropna()
df_gps['normal_date'] = pd.to_datetime(df_gps['timestamp'], unit='s')
df_gps = df_gps.sort_values('normal_date').reset_index(drop=True)

print(df_gps.head())

#Расстояние между точками (столбец distant)
distances = [0]

for i in range(1, len(df_gps)):
    point1 = (df_gps.iloc[i - 1]['lat'], df_gps.iloc[i - 1]['lon'])
    point2 = (df_gps.iloc[i]['lat'], df_gps.iloc[i]['lon'])
    distance_km = geodesic(point1, point2).kilometers
    distances.append(distance_km)

df_gps['distant (km)'] = distances

print(df_gps.head())

#Скорость между точками (столбец speed)
time = [0]

for i in range(1, len(df_gps)):
    time_count = df_gps.iloc[i]['timestamp'] - df_gps.iloc[i - 1]['timestamp']
    time.append(time_count)

df_gps['time (sec)'] = time
df_gps['speed (km/h)'] = df_gps['distant (km)'] / df_gps['time (sec)'] * 3600

print(df_gps.head())
df_gps.to_csv('data_new.csv', index=False)

#Направление движения в градусах (столбец direction):
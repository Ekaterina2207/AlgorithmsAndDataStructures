import pandas as pd
import numpy as np
import random

def gen_file(filename, num_rows=1000100):
    city = ['Москва', 'Санкт-Петербург', 'Омск', 'Пенза', 'Новосибирск', 'Орел', 'Сортавала', 'Владимир',
            'Калиниград', 'Лондон', 'Париж', 'Нью-Йорк', 'Вашингтон', 'Оттава', 'Торонто', 'Дели',
            'Пекин', 'Шанхай', 'Мумбаи', 'Минск', 'Орша', 'Якутск', 'Воркута', 'Ярославль', 'Смоленск',
            'Петрозаводск', 'Каир', 'Тбилиси', 'Тегеран', 'Дубай', 'Порту', 'Сан-Франциско']
    data = {
        'Город': np.random.choice(city, num_rows),
        'Население': np.random.randint(1000000, 12000000, num_rows),
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
gen_file('population.csv', 1000100)

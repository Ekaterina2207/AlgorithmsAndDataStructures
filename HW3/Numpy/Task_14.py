#Создать случайную матрицу 5x7 целых чисел от 1 до 100 и удалить [3,5] колонки

import numpy as np
array = np.random.randint(1, 101, (5, 7))
print(array)
array = np.delete(array, [3, 5], axis=1)
print()
print(array)
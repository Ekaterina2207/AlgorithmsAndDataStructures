#Создать массив 10x10 со случайными значениями, найти минимум и максимум

import numpy as np
array = np.random.randint(1,51,(10,10))
print(array)
print(np.max(array))
print(np.min(array))
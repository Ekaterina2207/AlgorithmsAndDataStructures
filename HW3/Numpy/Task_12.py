#Создать матрицу 8x8 и заполнить ее в шахматном порядке

import numpy as np
array = np.zeros((8,8), dtype=int)
array[::2,::2] = 1
array[1::2,1::2] = 1
print(array)

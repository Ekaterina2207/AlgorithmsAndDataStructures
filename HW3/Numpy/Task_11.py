#Создать матрицу с 0 внутри и 1 на границах

import numpy as np
array = np.zeros((5, 5), dtype=int)
array[0, :] = 1
array[-1, :] = 1
array[:, -1] = 1
array[:, 0] = 1
print(array)

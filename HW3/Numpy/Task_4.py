#Создать вектор заполненный нулями, но пятый элемент равен 1

import numpy as np
array = np.zeros(10, dtype = 'int32')
array[4] = 1
print(array)
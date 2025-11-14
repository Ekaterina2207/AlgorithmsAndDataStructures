#Найти индексы ненулевых элементов в [1,2,0,0,4,0]

import numpy as np
array = np.array([1,2,0,0,4,0])
indices = np.nonzero(array)
print(indices)
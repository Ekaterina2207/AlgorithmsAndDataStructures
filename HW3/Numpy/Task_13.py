#Перемножить матрицы 5x3 и 3x2

import numpy as np
matrix_1 = np.random.randint(1, 10, (5,3))
matrix_2 = np.random.randint(1, 10, (3,2))
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 @ matrix_2)
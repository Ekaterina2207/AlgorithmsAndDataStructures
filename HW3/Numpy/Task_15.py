#Есть генератор, сделать с его помощью массив

import numpy as np
def generate():
    for x in range(10):
        yield x
array = np.array(list(generate()))
print(array)

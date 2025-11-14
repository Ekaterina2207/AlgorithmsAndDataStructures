#Простой линейный график
#Построить график функции  y=x2  на отрезке [-10, 10]
#Добавить заголовок графика
#Подписать оси координат

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y, color='pink')
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('y=x2')
plt.grid(True)
plt.show()
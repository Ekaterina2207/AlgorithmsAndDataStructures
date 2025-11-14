#Несколько графиков
#Построить на одном графике функции синуса и косинуса
#Использовать разные цвета и стили линий

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y1 = np.cos(x)
y2 = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label = 'cos(x)', color = 'pink', linestyle='--')
plt.plot(x, y2, label = 'sin(x)', color = 'grey', linestyle=':')
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.grid(True)
plt.show()
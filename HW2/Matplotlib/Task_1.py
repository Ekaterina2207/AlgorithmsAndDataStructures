#Гистограмма
#Создать гистограмму распределения оценок студентов (данные: 4, 5, 3, 4, 5, 5, 4, 3, 2, 4)
import matplotlib.pyplot as plt

students = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
marks = [4, 5, 3, 4, 5, 5, 4, 3, 2, 4]

plt.bar(students, marks)
plt.title('Успеваемость')
plt.ylabel('Оценка')
plt.xlabel('Студент')
plt.show()
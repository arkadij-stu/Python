import matplotlib.pyplot as plt
subjects = ['Алгебра', 'Геометрия', 'Биология', 'ТеорВер', ]
marks = [4, 4, 4, 4]


plt.figure(figsize = (10, 10))
plt.scatter(subjects, marks, marker='s')
plt.xlabel('Предмет')
plt.ylabel('Оценка')
plt.yticks([2, 3, 4, 5])
plt.grid(True)
plt.show()
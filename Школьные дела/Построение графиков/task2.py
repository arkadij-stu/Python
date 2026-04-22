import matplotlib.pyplot as plt
dates = ['15.01', '16.01', '22.01', '23.01', '29.01', '05.02', '05.02', '07.02', '09.02', '22.02', '02.03', '09.03', '13.03']
marks = [5, 3, 4, 5, 3, 4, 2, 4, 3, 2, 5, 5, 3]


plt.figure(figsize = (10, 10))
plt.plot(dates, marks, marker='o')
plt.xlabel('Дата')
plt.ylabel('Оценка')
plt.grid(True)
plt.show()
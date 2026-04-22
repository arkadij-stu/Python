import matplotlib.pyplot as plt
hours = list(range(25))
tempr = [-2, -5, 0, 1, 3, 0, -1, 0, 2, 4, 6, 4, 2, 1, 0, -3, -6, -10, -9, -7, -8, -6, -5, -3, -4]
plt.figure(figsize = (12, 8))
plt.plot(hours, tempr, marker='o')
plt.xlabel('Час')
plt.ylabel('Температура,⁰C')
plt.xticks(hours)
plt.grid(True, linestyle=':')

plt.show()

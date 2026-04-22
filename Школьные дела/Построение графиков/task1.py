import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y1 = x ** 2
y2 = x ** 3 - 3 * x + 2

plt.figure(figsize = (10, 10))
plt.plot(x, y1, 'r', label = 'y = x²')
plt.plot(x, y2, 'b', label = 'y = x³ - 3x + 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

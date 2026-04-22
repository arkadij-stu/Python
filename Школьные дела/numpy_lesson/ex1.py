import numpy as np
arr1 = np.arange(1,16)
arr2 = np.random.randint(5, 16, arr1.shape)
product = arr1 * arr2
arr12 = arr1 ** 2
arr21 = arr2[arr2 >= 7]
print(arr1)
print(arr2)
print(product)
print(arr12)
print(arr21)

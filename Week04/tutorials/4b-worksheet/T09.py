import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = a # a and b reference to the same memory
b[0, 1] = 5
print(a)
print(b)

print()
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.copy()
b[0, 1] = 5
print(a)
print(b)

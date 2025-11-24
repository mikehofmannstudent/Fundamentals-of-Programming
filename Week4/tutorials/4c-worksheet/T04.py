import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(a.sum())
print(a.min())
print(a.max())
print(a.mean())
print()
print(a[:, 0])
print(a[:, 0].sum())
print(a[1, :])
print(a[1, :].sum())

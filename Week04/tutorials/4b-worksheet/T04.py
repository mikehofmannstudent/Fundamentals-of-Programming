import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.shape(a))
print(np.size(a))

d = a.reshape(3, 2)
print(d)
d = a.reshape(1, 6)
print(d)
d = a.reshape(6, 1)
print(d)

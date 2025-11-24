import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.shape(a))
print(np.size(a))

b = a.flatten()
print(np.shape(b))
print(np.size(b))
print(b)
c = a.flatten(order = 'F')
print(c)

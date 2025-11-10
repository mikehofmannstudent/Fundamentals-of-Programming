import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([6, 5, 4])

# compare each corresponding element
d = a < b
print(d)

#compare each element with 2
d = a < 2
print(d)

# compare each corresponding element
d = b == c
print(d)

# compare each corresponding element
d = b <= c
print(d)

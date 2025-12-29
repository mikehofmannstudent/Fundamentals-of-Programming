import numpy as np

a = np.matrix([[1, 2], [2, 3]])
b = np.matrix('1 -2; 2 3')
print(a)
print(b)

print()
r = a + b
print(r)
r = 5 * a
print(r)
r = a * b
print(r)
r = a**-1
print(r)

print()
r = np.linalg.det(a)
print(r)
r = b.T
print(r)

print()
e_val, e_vect = np.linalg.eig(a)
print(e_val)
print(e_vect)

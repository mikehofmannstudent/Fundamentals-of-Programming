import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
print(array1)
# array2 "reference" to part of array1
array2 = array1[1:3]
print(array2)

#changing array1 will affect array2
array1[2] = 100
print(array1)
print(array2)

# changing array2 will affect array1 too
array2[0] = 200
print(array1)
print(array2)

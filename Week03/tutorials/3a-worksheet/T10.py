import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
print(array1)

# array2 is a new array with content copied from array1
array2 = array1[1:3].copy()
print(array2)

#changing array1 will NOT affect array2
array1[2] = 100
print(array1)
print(array2)

# changing array2 will NOT affect array1
array2[0] = 200
print(array1) 
print(array2)

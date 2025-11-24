import numpy as np

listarray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], 
                      [9, 10, 11, 12]])

print(listarray[1:, 0])
print(listarray[2, 1:])
print(listarray[2, :])
print(listarray[:, ::2])

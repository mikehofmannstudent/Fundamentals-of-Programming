import numpy as np

numarray = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
                     [9, 10, 11, 12]])

print("Shape is: ", np.shape(numarray))
print("Number of rows: ", len(numarray[:, 0]))
print("Number of cols: ", len(numarray[0, :]))

row, col = 0, 0
while row < len(numarray[:, 0]):
    while col < len(numarray[0, :]):
        print("Element [", row, ",", col, "] is: ", numarray[row, col])
        col += 1
    row += 1
    col = 0

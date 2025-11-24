import numpy as np

numarray = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
                     [9, 10, 11, 12]])

for row in numarray:
    for element in row:
        print("Element: ", element)

print()
for rindex, row in enumerate(numarray):
    for cindex, element in enumerate(row):
        print("Element: [", rindex, ",", cindex, "] is: ", element)

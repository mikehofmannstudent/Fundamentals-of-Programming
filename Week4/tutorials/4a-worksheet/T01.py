import numpy as np

print()
arangearray = np.arange(0, 20, 2)
print(arangearray)

print()
linarray = np.linspace(0, 1, 6)
print(linarray)

print()
linarray = np.linspace(0, 1, 5, endpoint = False)
print(linarray)

print()
array1 = np.array([1, 2, 3, 4])
print(array1[0])
r = array1[2] + array1[3]
print(r)

print()
array2 = np.array([1, 2, 3, 4])
for index in range(len(array2)):
    print(array2[index])

print()
for value in array2:
    print(value)

array3 = np.array([1, 2, 3, 4])
print(array3[1:3])
print(array3[:3])
print(array3[1:])
print(array3[::-1])

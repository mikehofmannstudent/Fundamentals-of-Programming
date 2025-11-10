import numpy as np

array = np.arange(0, 5)

# while loop
index = 0
while index < len(array):
    print("Element ", index, " is: ", array[index])
    index += 1
print()

# for with index
for index in range(0, len(array)):
    print("Element ", index, " is: ", array[index])
print()

# for each
for item in array:
    print("Element is: ", item)

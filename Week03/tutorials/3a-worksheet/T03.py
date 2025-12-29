import numpy as np

# Accessing elements
array1 = np.array([1, 2, 3])
print(f"index0: {array1[0]}")
array1[0] = 5
print(f"index 0: {array1[0]}")

# Access parts of the array with slicing:
array1 = np.array([1, 2, 3, 4, 5])
# Similar to how wto slice a list
print(array1[1:3]) # index 1 to 2

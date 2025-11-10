import numpy as np

names = np.array(['John', 'Peter', '´Bob'])
scores = np.array([45, 52, 80])

# Comparison results
print(scores >= 50)

# Pass - put the comparison into the names array
# to filter out the "True" element
print(scores[scores >= 50])
print(names[scores >= 50])

import numpy as np

zeroarray = np.zeros((3, 3, 3))
print(zeroarray)
print(np.size(zeroarray))

zeroarray.resize((1, 27))
print(zeroarray)
print(np.size(zeroarray))

zeroarray.resize((3, 9))
print(zeroarray)
print(np.size(zeroarray))

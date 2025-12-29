import numpy as np

bigarray = np.arange(0, 64)
print(np.size(bigarray))
print(bigarray)

bigarray.resize(4, 4, 4)
print(bigarray)

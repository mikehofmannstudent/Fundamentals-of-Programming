from scipy import datasets
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

face = datasets.face()
size_org = np.shape(face)
print(size_org)
plt.imshow(face)
plt.show()

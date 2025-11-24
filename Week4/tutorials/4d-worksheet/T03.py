from scipy import datasets
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

face = datasets.face(gray = True)
plt.imshow(face, cmap = plt.cm.gray)
plt.show()

from scipy import datasets
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

face = datasets.face(gray = True)
shifted_face = ndimage.shift(face, (150, 50))
plt.imshow(shifted_face)
plt.show()

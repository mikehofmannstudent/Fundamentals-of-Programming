from scipy import datasets
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

face = datasets.face(gray = True)
rotated_face = ndimage.rotate(face, 30)
plt.imshow(rotated_face)
plt.show()

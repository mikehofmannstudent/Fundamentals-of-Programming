from scipy import datasets
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

face = datasets.face(gray = True)
cropped_face = face[100:500, 400:800]
plt.imshow(cropped_face)
plt.show()

from scipy import datasets
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

face = datasets.face(gray = True)
pixel_face = face[::10, ::10]
size_pixelled1 = np.shape(pixel_face)
print(size_pixelled1)
plt.imshow(pixel_face)
plt.show()

pixel_face = face[::50, ::50]
size_pixelled2 = np.shape(pixel_face)
print(size_pixelled2)
plt.imshow(pixel_face)
plt.show()

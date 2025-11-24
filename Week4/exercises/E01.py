import numpy as np
import matplotlib.pyplot as plt 
from scipy import ndimage
from scipy import datasets

face = datasets.face(gray = True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

# i.
croppedFace = face[100:-100, 50:-50]
plt.imshow(croppedFace, cmap=plt.cm.gray)
plt.show()

# ii.
pixelFace = face[50::10, 100::10]
plt.imshow(pixelFace, cmap=plt.cm.gray)
plt.show()

# iii.
rotatedFace = ndimage.rotate(face, 110)
plt.imshow(rotatedFace, cmap=plt.get_cmap('Reds'))
plt.show()

import numpy as np 
import matplotlib.pyplot as plt
ar1 = np.arange(0., 5., 0.2)
ar2 = ar1**2
ar3 = ar1**3
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
plt.figure(1)
plt.subplot(131)
plt.plot(x_values, ar1, 'r--')
plt.subplot(132)
plt.plot(x_values, ar2, 'bs')
plt.subplot(133)
plt.plot(x_values, ar3, 's')
plt.show()

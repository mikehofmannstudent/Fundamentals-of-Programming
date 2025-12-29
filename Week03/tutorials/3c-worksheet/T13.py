import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal

# generate 1000 random data from normal distribution
gaussian_numbers = normal(size = 1000)
# plot the 1000 random data on a histogram

plt.hist(gaussian_numbers, 
         bins = 20, density = True,
         cumulative = True, color = ['purple'])

plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal

# generate 1000 random data from normal distribution
gaussian_numbers = normal(size = 1000)
# plot the 1000 random data on a histogram
# change the graph type to be a step outline rather than filled in
plt.hist(gaussian_numbers, histtype = 'step')

plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

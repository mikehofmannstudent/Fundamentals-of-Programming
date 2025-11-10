import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal

# generate 1000 random data from normal distribution
gaussian_numbers = normal(size = 1000)
# plot the 1000 random data on a histogram
# set the number of bins is 20
# make the graph cumulative
plt.hist(gaussian_numbers, bins = 20, cumulative = True)

plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

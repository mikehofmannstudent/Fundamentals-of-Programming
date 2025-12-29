import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal

# generate 1000 random data from normal distribution
gaussian_numbers = normal(size = 1000)

# plot the 1000 random data on a histogram
# note: the default number of bins is 10
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# bar chart example
xValues = [1, 2, 3, 4, 5, 6]
yValues = [4, 7, 5, 3, 2, 1]
width = 0.9
plt.bar(xValues, yValues, width, color = 'purple')
plt.show()

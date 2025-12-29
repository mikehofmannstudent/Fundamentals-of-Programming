import numpy as np

# Adding GST example
prices = np.array([12.3, 17.8, 3.2, 4.3, 50])
gstprices = np.round(prices * 1.08, 2)
print(gstprices)

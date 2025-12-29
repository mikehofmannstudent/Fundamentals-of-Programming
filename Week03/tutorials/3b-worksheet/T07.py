import numpy as np

# exchange rate example
usdprices = np.array([10, 20, 30, 40, 50])
exchrate = 1.3
audprices = usdprices * exchrate
print(audprices)

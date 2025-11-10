import numpy as np

# Preset arrays
# Create an array of 10 float (default), all = 0
zeroarray = np.zeros(10)
print(zeroarray)
# Create an array of 10 int all = 0
zeroarray = np.zeros(10, dtype = int)
print(zeroarray)

# Create an rray of 10 float (defaults), all set to 1
onesarray = np.ones(10)
print(onesarray)
# Create an array od 10 intigers, all set to 1
onesarray = np.ones(10, dtype = int)
print(onesarray)

# Create an array with size of 10
# each element is 5
tens = np.full(10, 5)
print(tens)

# Array of 10 ranfom numbers (0 to 0.999...)
rarray = np.random.random(10)
print(rarray)

# Replace all the elements in rarray with 10
rarray.fill(10)
print(rarray)

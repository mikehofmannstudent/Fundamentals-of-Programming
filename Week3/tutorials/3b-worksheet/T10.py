import numpy as np

# Min and Max example
# generate 50 random numbers between 10 and 80
r_numbers = np.random.uniform(low = 10, high = 80, size = (50,))
print(r_numbers)
# print the num random numbers generated
print(r_numbers.min())
# print the max random numbers generated
print(r_numbers.max())

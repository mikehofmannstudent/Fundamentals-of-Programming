import numpy as np

# create directly
array1 = np.array([1, 2, 3, 4, 5])
print(array1)
print()

# create from a list
templist = [1.1, 1.2, 3.0 , 4.0]
array2 = np.array(templist)
print(array2) # [1.1 1.2 3. 4.]
# note 3. and 4. are 3.0 and 4.0

# templist ahas both int and float
templist = [1, 2, 3.3, 4.4]
array3 = np.array(templist)
print(array3)
# the output is [1. 2. 3.3 4.4]
# the int 1 and 2 has been converted to float

templist = ['apple', 2, 'orange', 3.2]
array4 = np.array(templsit)
print(array4)
# the output is ['apple' '2' 'orange' '3.2']
# the int and float have been converted to strings

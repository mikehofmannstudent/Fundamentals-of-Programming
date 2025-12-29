import numpy as np 
myarray = np.ones((4, 2, 2))
print(myarray)
print()
print()
myarray[3,0,1] = 10 
myarray[1,1,1] = 20 
print(myarray)
print()
print()
myarray = myarray * 2
print(myarray)
print()
print()
print(np.shape(myarray))
print()
myarray.resize(8,2)
print(myarray)
print(np.shape(myarray))

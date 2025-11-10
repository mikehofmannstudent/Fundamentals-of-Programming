import numpy as np

# gives an array [0 1 2 3  4 5 6 7 8 9]
myarray = np.arange(0, 10)
print (myarray)

print(myarray[1:3])

print(myarray[:3])

print(myarray[3:])

print(myarray[3::2])

print(myarray[::2])

tofifty = np.linspace(0, 50, 5)
print(tofifty)

tofifty2 = tofifty[1:3]
print(tofifty2)

tofifty3 = tofifty[::2]
print(tofifty3)

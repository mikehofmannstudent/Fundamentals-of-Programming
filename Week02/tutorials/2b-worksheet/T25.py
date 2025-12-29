#        012345678901234
names = "Ada Bob Charles"

name1 = names[0:3] # slice index 0 to 2 (3-1)
print(name1) # Ada

name2 = names[4:7] # slice index 4 to 6 (7-1)
print(name2) # Bob

name3 = names[8:] # slice index 8 to the end
print(name3) # Charles

name4 = names[:3] # slice from start to 2
print(name4) # Ada

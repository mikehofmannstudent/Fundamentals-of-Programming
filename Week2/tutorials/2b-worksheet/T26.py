#        012345678901234
names = "Ada Bob Charles"

# slice index 0 to the end with spets of 2
# index -> 0 2 4 6 8 10 12 14
name5 = names[::2]
print(name5) # AaBbCals

# slice index 8 to the end with steps of 2
# index -> 8 10 12 14
name6 = names[8::2]
print(name6) #Cals

# slice index 0 to 10 with steps of 2
# index -> 0 2 4 6 8 10
name7 = names[:11:2]
print(name7) # AaBbCa

mealset1 = ['egg', 'bacon']
mealset2 = ['sausage', 'bacon', 'kiwi']
mealset3 = ['spam', 'egg', 'bacon']

# put three lists into on list
mealsets = [mealset1, mealset2, mealset3]
print(mealsets)
print()

# retrieve mealset2 with index of 1
print(mealsets[1])
print()

# retrieve item 2 (index 1)
# in measet 3 (index 2)
print(mealsets[2][1]) # egg
print()

# loop the 2D list
for mealset in mealsets:
    print(mealset)

set_data = ['apple', 'orange', 'kiwi']
set_fruits = set(set_data)

print(set_fruits)
print(type(set_fruits))
print()

set_fruits2 = {'apple', 'pinapple', 'orange'}
print(set_fruits2)
print(type(set_fruits2))


pythonlist = ['John', 'Eric', 'Graham', 'Terry', 'Michael', 'Terry']
pythonset = set(pythonlist)
goodieslist = ['Bill', 'Graham', 'Tim']
goodiesset = set(goodieslist)
print(pythonset)
print(goodiesset)
print("Intersection = ", pythonset.intersection(goodiesset))
print("Union = ", pythonset.union(goodiesset))
print("Difference = ", pythonset.difference(goodiesset))
print("Difference = ", goodiesset.difference(pythonset))

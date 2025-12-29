names = open('names.txt')

# a list, one line per element
thischunk = names.readlines()
print(thischunk)
names.close()

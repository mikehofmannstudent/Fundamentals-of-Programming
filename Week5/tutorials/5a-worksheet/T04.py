# open the file for reading
names = open('names.txt')

# reads entire contents of file
thischunk = names.read()
print(thischunk)

# close the file
names.close()

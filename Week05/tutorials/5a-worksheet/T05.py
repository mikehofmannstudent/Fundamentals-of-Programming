names = open('names.txt')

# read one line (first line)
thischunk = names.readline()
print(thischunk, end = '')

# read another line (second line)
thischunk = names.readline()
print(thischunk, end = '')
names.close()

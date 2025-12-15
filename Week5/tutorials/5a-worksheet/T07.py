# f represents the file (file pointer)
with open('names.txt') as f:
    read_data = f.readlines()
    for line in read_data:
        print(line, end = '')

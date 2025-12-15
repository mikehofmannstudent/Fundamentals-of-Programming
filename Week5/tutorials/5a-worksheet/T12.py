try:
    with open('myfile.txt') as f:
        read_data = f.readlines()
        for line in read_data:
            print(line, end = '')
except OSError as err:
    print("OS error:", err)

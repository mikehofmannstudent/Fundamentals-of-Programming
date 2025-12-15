with open('results.csv') as f:
    data = f.readlines()
    for line in data:
        line = line.strip()
        linelist = line.split(',')
        for record in linelist:
            print(record, end = ' ')
        print()

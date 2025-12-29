hlist = []
fileobj = open('heatsource.csv', 'r')
for line in fileobj:
    line_s = line.strip()
    ints = [int(x) for x in line_s.split(',')]
    hlist.append(ints)
fileobj.close()

print(hlist)

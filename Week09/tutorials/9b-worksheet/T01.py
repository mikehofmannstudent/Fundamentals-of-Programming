tup1 = ('spam', 'eggs', 42)
tup2 = (1, 4, 6, 16, 25)
tup3 = 'yes', 'oui', 'ja', 'si'

print(tup1)
print(tup2)
print(tup3)

print()
print("Slice")
print(tup1[2])
print(tup2[1:-1])

print("Loop")
for i in tup3:
    print(i)

    print("Concatenate")
    print(tup1 + tup2)

    print("Duplicate")
    print(tup1 * 2)

    print("Length of tuple")
    print(len(tup2))
    

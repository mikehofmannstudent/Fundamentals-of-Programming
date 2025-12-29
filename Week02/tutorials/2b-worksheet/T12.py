names = "Ada Bob Charles"

for i in range(len(names)):
    print(names[i])

# note:
# len(names) => 15
# range(len(names)) => range(15)
# range(15) => [0, 1, 2, ..., 14]

print()
for i in range(len(names) - 1, -1, -1):
    print(names[i])

# note:
# range(len(names)-1, -1, -1) => range(15-1, -1, -1)
# range(15 - 1, -1, -1) => range(14, -1, -1)
# range(14, -1, -1) => [14, 13, ..., 0]

print()
for i in range(0, len(names), 2):
    print(names[i])

# note:
# range(0, len(names), 2) => range(0,15,2)
# range(0, 15, 2) => [0, 2, 4, ..., 14]

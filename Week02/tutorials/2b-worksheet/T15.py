names = "Ada Bob Charles"

for letter in names:
    print(letter, end="") # will not print \n

print()

for letter in names:
    print(letter, end="*") # will print * at the end

print()

for letter in names:
    print(letter) # will print \n

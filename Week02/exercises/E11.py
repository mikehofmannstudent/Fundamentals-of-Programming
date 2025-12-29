instring = input("Enter a string: ")

instring = instring.upper()

newString1 = ''
for char in range(2, len(instring), 4):
    newString1 += instring[char]
print(newString1)

newString2 = instring[3:-1:3]
print(newString2)

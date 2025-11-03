instring = input("Enter a string: ")

instringLower = instring.lower()
print(instringLower)

i = 2
newString1 = ""
while i < len(instring):
    newString1 += instring[i]
    i += 3
print(newString1)

newString2 = instring[::-1]
newString2 = newString2[1:-1:5]
print(newString2)

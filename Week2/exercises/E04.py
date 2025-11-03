n = 5

for i in range(n):
    print("A|" * 5)

print()

for i in range(n):
    print("+=" * (i + 1))

print()

for i in range(n):
    print("B|" * (5 - i))
    
print()

for i in range(n):
    print((":>" * (5 - i)) + "  " + (":P" * (i + 1)))

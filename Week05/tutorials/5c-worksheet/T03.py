numbers = [1, 2, 3, 4, 5]

doubledOdds = []
for n in numbers:
    if n % 2 == 1:
        doubledOdds.append(n * 2)
print(doubledOdds)

print()
doubledOdds = [n * 2 for n in numbers if n % 2 == 1]
print(doubledOdds)

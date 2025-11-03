animals = ['fish', 'cat', 'dog', 'lion', 'tiger', 'mouse', 'cow']

for animal in animals:
    print(animal)

print()

animals.reverse()
for animal in animals:
    print(animal)

print()
animals.reverse()

animals = [animal[:3] for animal in animals]
for animal in animals:
    print(animal)

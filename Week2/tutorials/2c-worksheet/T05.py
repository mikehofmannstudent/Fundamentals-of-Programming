import random

fruits = ['apple', 'orange', 'kiwi']

for i in range(10):
    fruit = random.choice(fruits)
    print(fruit)


sides = [0, 1]
heads = 0
tails = 0

for i in range(1000):
    if(random.choice(sides) == 0):
        heads += 1
    else:
        tails += 1

print("Heads =  ", heads)
print("Tails = ", tails)

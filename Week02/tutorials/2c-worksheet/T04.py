import random

# range(0, 11, 5) => [0, 5, 10]
print(list(range(0, 11, 5)))

#print 5 random from range(0, 11, 5) => [0, 5, 10]
for i in range(5):
    print(random.randrange(0, 11, 5))

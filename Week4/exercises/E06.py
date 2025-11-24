import random

def randomString(list):
    randomItem = list[random.randint(0, (len(list) - 1))]
    return randomItem


list = []
for i in range(1,5):
    num = int(input(f"Enter a number ({i}/4): "))
    list.append(num)

print(randomString(list))

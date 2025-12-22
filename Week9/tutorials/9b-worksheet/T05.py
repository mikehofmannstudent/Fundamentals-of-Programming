import random
import matplotlib.pyplot as plt

dicecount = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(1000):
    toss = random.randint(1, 6)
    dicecount[toss] += 1

plt.bar(dicecount.keys(), dicecount.values())
plt.show()

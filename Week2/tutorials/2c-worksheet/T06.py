import random

numTrials = 1000000
ncirc = 0 # no. of hits on circle
r = 1.0 # radius of circle
r2 = r * r

for i in range(numTrials):
    # generate random x y to represent where the dart lands
        x = random.random()
        y = random.random()
        if((x * x + y * y) <= r2): # dart lands on the circle
            ncirc += 1 # increase no. of hits on the circle by 1

# Note: all darts will land on the square
# so no. of hitson the square is numTrails
pi = 4.0 * ncirc / numTrials
print("\nFor ", numTrials, " trials, pi = ", pi)

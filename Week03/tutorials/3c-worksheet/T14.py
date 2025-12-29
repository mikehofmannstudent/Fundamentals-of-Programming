# growth.py - simulation of unconstrained growth
import matplotlib.pyplot as plt
print("\nSIMULATION - Unconstrained Growth\n")
length = 100
population = 100
growthRate = 0.1
timeStep = 0.5
numIter = length / timeStep
growthStep = growthRate * timeStep

print("INITAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Poluation: ", population)
print("Groth Rate (per hour): ", growthRate)
print("Time Step (part hour per step): ", timeStep)
print("Num iterations (length  * timestep / hour)", numIter)
print("Growth step (growthrate per timestep): ", growthStep)
print("\nRESULTS\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)
times = [0]
pops = [100]

for i in range(1, int(numIter) + 1):
    growth = growthStep * population
    population += growth
    time = i * timeStep
    times.append(time)
    pops.append(population)
    print("Time: ", time, " \tGrowth: ", growth, " \tPopulation: ", population)

print("\nPROCESSING COMPLETE\n")
plt.title("Unconstrained Growth")
plt.plot(times, pops)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

size = 10
currg = np.zeros((size, size))
print(currg)

currg[:, 0] = 10

nextg = np.zeros((size, size))

for timestep in range(5):
    for r in range(1, size - 1):
        for c in range(1, size - 1):
            # calculate each cell head using the heat diffusion formula
            # use Von Neuman neighbourhood
            # note the ratio for each cell should add up to 1
            north = currg[r - 1, c] * 0.1
            northeast = currg[r - 1, c + 1] * 0.1
            east = currg[r, c + 1] * 0.1
            southeast = currg[r + 1, c + 1] * 0.1
            south = currg[r + 1, c] * 0.1
            southwest = currg[r + 1, c - 1] * 0.1
            west = currg[r, c - 1] * 0.1
            northwest = currg[r - 1, c - 1] * 0.1
            center = currg[r, c] * 0.2
            nextg[r, c] = north + northeast + east + southeast + south + southwest + west + northwest + center
    nextg[:, 0] = 10
    print("Time step: ", timestep)
    print(nextg)
    currg = nextg.copy()
    plt.title("Heat Diffusion Simulation: Time step: " + str(timestep))
    plt.imshow(currg, cmap = plt.cm.hot)
    plt.colorbar()
    plt.show()

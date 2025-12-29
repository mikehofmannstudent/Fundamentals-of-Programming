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
            nextg[r, c] = 0.1 * currg[r - 1:r + 2, c - 1:c + 2].sum() + 0.1 * currg[r, c]
    nextg[:, 0] = 10
    print("Time step: ", timestep)
    print(nextg)
    currg = nextg.copy()
    plt.title("Heat Diffusion Simulation: Time step: " + str(timestep))
    plt.imshow(currg, cmap = plt.cm.hot, interpolation = 'bilinear')
    plt.colorbar()
    plt.show()

import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
t2 = t ** 2
t3 = t ** 3

plt.title("Multiline")
# three data sets on one plot
plt.plot(t, t, 'r--',
         t, t2, 'bs', 
         t, t3, 'g^')
# 'r--' => red dashes
# 'bs' => blue squares
# 'g^' => green triangles
plt.show()

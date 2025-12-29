import matplotlib.pyplot as plt
import numpy as np

march2017 = np.array([37.7, 29.9, 35.2,
                    36.1, 37.2, 34.7, 33.8, 34.5, 31.9, 29.9, 
                    30.9, 24.8, 24.2, 24.1, 24.0])
dates = range(1, len(march2017) + 1)

# dates - x values
# march2017 - y values
plt.plot(dates, march2017)

plt.title("March Temperatures")
plt.ylabel("Temerature")
plt.xlabel("Date")
plt.show()

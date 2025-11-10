import matplotlib.pyplot as plt
import numpy as np

# Subplots 2 by 1
march2017 = np.array([37.7, 29.9, 35.2, 36.1, 36.2, 
                       34.7, 33.8, 34.5, 31.9, 29.9, 30.9, 
                       24.8, 24.2, 24.1, 24.0])

dates = range(1, len(march2017) + 1)
plt.figure(1)
plt.subplot(211) # 2 rows, 1 col, subplot 1
plt.plot(dates, march2017, '--')
plt.title("March Temperatures")
plt.ylabel("Temperature")

plt.subplot(212) # 2 rows, 1 col, subplot 2
plt.plot(dates, march2017, 'ro')
plt.ylabel("Temperature")
plt.xlabel("Date")
plt.show()

# Subplots 2 by 2
march2017 = np.array([37.7, 29.9, 35.2, 36.1, 36.2, 
                      34.7, 33.8, 34.5, 31.9, 29.9, 
                      30.9, 24.8, 24.2, 24.1, 24.0])
dates = range(1, len(march2017) + 1)

plt.figure(2)
plt.subplot(221)
plt.plot(dates, march2017, '--')
plt.title("March Temperatures")
plt.ylabel("Temperature")
plt.subplot(222)
plt.plot(dates, march2017, 'ro')
plt.ylabel("Temperature")
plt.ylabel("Date")
plt.subplot(223)
plt.plot(dates, march2017, 'g^')
plt.ylabel("Temperature")
plt.xlabel("Date")
plt.subplot(224)
plt.plot(dates, march2017, 'bs')
plt.ylabel("Temperature")
plt.xlabel("Date")

plt.show()

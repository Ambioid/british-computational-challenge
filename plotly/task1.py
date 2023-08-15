import matplotlib.pyplot as plt
import numpy as np

orbitalPeriod = np.array([0.241, 0.615, 1.000, 1.881, 11.861, 29.628, 84.727, 166.344, 248.348])
semiMajorAxis = np.array([0.387, 0.723, 1.000, 1.523, 5.202, 9.576, 19.293, 30.246, 39.509])

semiMajorAxis = np.power(semiMajorAxis, 3/2)

plt.plot(semiMajorAxis, orbitalPeriod)
plt.plot(semiMajorAxis, orbitalPeriod, 'o')
plt.show()


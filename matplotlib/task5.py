#Numeric method to compute polar angle vs orbit time
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
    
def angle_vs_time(t ,P ,ecc ,theta0): 
    dtheta = 1 / 1000
    
    #Number of orbits
    N = np.ceil(t[-1] / P)
    
    #Define array of polar angles for orbits
    theta = np.arange(theta0,(2 * np.pi * N + theta0)+dtheta,dtheta)
    
    #Evaluate integrand of time integral
    f = (1 - ecc * np.cos(theta)) ** (- 2)
    
    #Define Simpson rule coefficients c = [ 1, 4, 2, 4, 2, 4, ....1 ]
    L = len(theta)
    c =  [1] + [4 if (x % 2 == 0) else 2 for x in range(L-2)] + [1]

    #Calculate array of times
    tt = np.multiply(P * ((1 - ecc ** 2) ** (3 / 2)) * (1 / (2 * np.pi)) * dtheta * (1 / 3),np.cumsum(np.multiply(c,f)))
    #Interpolate the polar angles for the eccentric orbit at the circular orbit
    #times
    theta = interpolate.splrep(tt,theta)
    print(len(tt), len(theta), len(t))
    # plt.plot(tt, theta)
    # return ("tt:", tt, "Theta:", theta)
    return theta

# plt.plot([0,1,2,3], angle_vs_time([0,1,2,3], 248, 0.25, 0), 'o', color="red")
plot = angle_vs_time(list(range(800)), 248, 0.25, 0)
plt.plot(plot[0][:-4], plot[1][:-4], color="Green", label="Eccentricity=0.25")

plot = angle_vs_time(list(range(800)), 248, 0.00, 0)
plt.plot(plot[0][:-4], plot[1][:-4], color="Blue", label="Eccentricity=0.00")

plt.legend(loc='upper left')
plt.title("Orbit Angle vs Time (Pluto)")
plt.xlabel("Time (Years)")
plt.ylabel("orbital polar angle (Radians)")

plt.show()
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')


def ellipse_3d(major_axis, eccentricity, inclination, name, color):
    tracex = [] 
    tracey = []
    tracez = []

    for i in range(1000):
        x = i*360/999
        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
        tracex.append(radius*np.cos(math.radians(x))*np.cos(math.radians(inclination)))
        tracey.append(radius*np.sin(math.radians(x)))
        tracez.append(radius*np.cos(math.radians(x))*np.sin(math.radians(inclination)))

    # return ax.plot(tracex, tracey, tracez)
    ax.plot3D(tracex, tracey, tracez, label=name, color=color)



def animate_3d(frame):
    for i in range(len(planets)):
        major_axis, period, eccentricity, inclination, name, color,= planets[i][0], planets[i][2], planets[i][1], planets[i][3], planets[i][4], planets[i][5]

        x = (2*math.pi*frame*100)/period

        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
        tracex = (radius*np.cos(math.radians(x))*np.cos(math.radians(inclination)))
        tracey = (radius*np.sin(math.radians(x)))
        tracez = (radius*np.cos(math.radians(x))*np.sin(math.radians(inclination)))


        markers_3d[i].set_data(tracex, tracey)
        markers_3d[i].set_3d_properties(tracez)
    print(frame)
    return markers_3d

    # for line, walk in zip(lines, walks):
    #     # NOTE: there is no .set_data() for 3 dim data...
    #     line.set_data(walk[:num, :2].T)
    #     line.set_3d_properties(walk[:num, 2])
    # return lines



planets = [ #Major axis, eccentricity, period, inclination, name, color
    # [0.387, 0.21, 0.241,  7.00, "Mercury", "grey",   ],
    # [0.723, 0.01, 0.615,  3.39, "Venus",   "#f5c753", ],
    # [1.000, 0.02, 1.000,  0.00, "Earth",   "blue",   ],
    # [1.523, 0.09, 1.881,  1.85, "Mars",    "red",    ],
    [5.202,   0.05, 11.861,  1.31, "Jupiter", "#f5e253"],
    [9.576,   0.06, 29.628,  2.49, "Saturn",  "orange"],
    [19.293,  0.05, 84.747,  0.77, "Uranus",  "lightblue"],
    [30.246,  0.01, 166.344, 1.77, "Neptune", "blue"],
    [39.509,  0.25, 248.348, 17.5, "Pluto", "peru"],
] 

for i in range(len(planets)): #Create an ellipse for every planet
    ellipse_3d(planets[i][0], planets[i][1], planets[i][3], planets[i][4], planets[i][5])

markers_3d = []
for i in range(len(planets)): # Create a marker for every planet
    markers_3d.append(ax.plot([], [], [], 'o', color=planets[i][5])[0])
    print(type(markers_3d[i]))
    # markers_3d.append(ax.plot([].[])

# print(type(ax.plot(0, 0, 0, "o", color=planets[i][5])[0]))

# orbits = [ellipse(planets[i][0], planets[i][1], planets[i][3], planets[i][4], planets[i][5]) for i in range(len(planets))]
# lines = [ax.plot([], [], [])[0] for _ in orbits]

ax.legend(loc='upper left')
ani = FuncAnimation(fig, animate_3d, interval=100, blit=True)

# ani = FuncAnimation(fig, animate, interval=100)
ax.set(xlabel='x/AU', xlim=(-40, 40))
ax.set(ylabel='y/AU', ylim=(-40, 40))
ax.set(zlabel='z/AU', zlim=(-40, 40))
plt.show()


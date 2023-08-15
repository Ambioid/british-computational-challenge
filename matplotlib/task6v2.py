import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count


def ellipse(major_axis, eccentricity, name, color):
    tracex = [] 
    tracey = []

    for i in range(1000):
        x = i*360/999
        # x = (2*math.pi*i/9)/period

        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*math.cos(math.radians(x))))
        tracex.append(radius*math.cos(math.radians(x)))
        tracey.append(radius*math.sin(math.radians(x)))
    
    plt.plot(tracex, tracey, label=name, color=color)

def draw_all(frames):
    
    
    for frame in range(frames):
        posx, posy = [], []
        speed = .5
        for i in range(len(planets)):
            
            major_axis, period, eccentricity, name, color,= planets[i][0], planets[i][2], planets[i][1], planets[i][3], planets[i][4]

            x = (2*math.pi*frame*speed)/period

            radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*math.cos(math.radians(x))))
            tracex = (radius*math.cos(math.radians(x)))
            tracey = (radius*math.sin(math.radians(x)))
            
            posx.append(tracex)
            posy.append(tracey)

            # plt.plot(tracex, tracey, 'o', color=color)

        plt.plot(posx, posy, linewidth=0.15, color="black", )
        print(frame)      
        

planets = [ #Major axis, eccentricity, period, name, color, tracex, tracey
    # [0.387, 0.21, 0.241, "Mercury", "grey",   ],
    [0.723, 0.01, 0.615, "Venus",   "#f5c753", ],
    [1.000, 0.02, 1.000, "Earth",   "blue",   ],

    [1.523, 0.09, 1.881, "Mars",    "red",    ],
    # [5.202,   0.05, 11.861, "Juipter", "#f5e253"],
    # [9.576,   0.06, 29.628, "Saturn",  "orange"],

    # [19.293,  0.05, 84.747, "Uranus",  "lightblue"],
    # [30.246,  0.01, 166.344,"Neptune", "blue"],
    # [39.509,  0.25, 248.348,"Pluto", "peru"],
]


index = count()
plt.figure(figsize=(8,8))
plt.legend(loc='upper left')
plt.xlabel("x/AU")
plt.ylabel("y/AU")
plt.grid()

for i in range(len(planets)):
    ellipse(planets[i][0], planets[i][1], planets[i][3], planets[i][4])

draw_all(1200)

plt.show()
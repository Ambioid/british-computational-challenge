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

def animate(frame):
    plt.cla()
    speed = 1

    major_axis, period, eccentricity, name, color,= center[0], center[2], center[1], center[3], center[4]


    x = (2*math.pi*frame*speed)/period
    radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*math.cos(math.radians(x))))
    currentx = (radius*math.cos(math.radians(x)))
    currenty = (radius*math.sin(math.radians(x)))

    for i in range(len(planets)):
        
        major_axis, period, eccentricity, name, color, tracex, tracey = planets[i][0], planets[i][2], planets[i][1], planets[i][3], planets[i][4],planets[i][5],planets[i][6],

        x = (2*math.pi*frame*speed)/period

        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*math.cos(math.radians(x))))
        tracex.append(radius*math.cos(math.radians(x)) - currentx)
        tracey.append(radius*math.sin(math.radians(x)) - currenty)
        
        plt.plot(tracex, tracey, color=color, label=name)

    # plt.plot(posx, posy, linewidth=0.25, color="black", )
    
    print(frame)
    plt.legend(loc='upper left')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)

    plt.xlabel("x/AU")
    plt.ylabel("y/AU")



planets = [ #Major axis, eccentricity, period, name, color, tracex, tracey
    [0.000,   0.00, 0.001,  "Sun",     "yellow",   [], []],
    [0.387,   0.21, 0.241,  "Mercury", "grey",     [], []],
    # [0.723,   0.01, 0.615,  "Venus",   "#f5c753",  [], []],
    [1.000,   0.02, 1.000,  "Earth",   "blue",     [], []],
    [1.523,   0.09, 1.881,  "Mars",    "red",      [], []],
    # [5.202,   0.05, 11.861, "Juipter", "#f5e253",  [], []],
    # [9.576,   0.06, 29.628, "Saturn",  "orange",   [], []],
    # [19.293,  0.05, 84.747, "Uranus",  "lightblue",[], []],
    # [30.246,  0.01, 166.344,"Neptune", "blue",     [], []],
    # [39.509,  0.25, 248.348,"Pluto",   "peru",     [], []],
]


center = 2
center = planets.pop(center)

index = count()

plt.figure(figsize=(10, 10))
plt.style.use('dark_background')
ani = FuncAnimation(plt.gcf(), animate, interval=10)


plt.show()
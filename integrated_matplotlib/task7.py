import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import numpy as np


def task7():
    plt.style.use('dark_background')
    fig = plt.Figure(dpi=100)
    ax = fig.add_subplot()


    def animate(frame):
        # plt.cla()
        
        # print(traces)
        major_axis, period, eccentricity= center[0], center[2], center[1]


        x = (2*math.pi*frame*speed)/period
        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*math.cos(math.radians(x))))
        currentx = (radius*math.cos(math.radians(x)))
        currenty = (radius*math.sin(math.radians(x)))

        for i in range(len(planets)):
            
            major_axis, period, eccentricity, name, color= planets[i][0], planets[i][2], planets[i][1], planets[i][3], planets[i][4]#,planets[i][5],planets[i][6],

            x = (2*math.pi*frame*speed)/period

            radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*math.cos(math.radians(x))))
            
            
            # tracex = np.append(traces[i].get_xdata(), radius*math.cos(math.radians(x)) - currentx)
            # tracey = np.append(traces[i].get_ydata(), radius*math.sin(math.radians(x)) - currenty)

            tracex = radius*math.cos(math.radians(x)) - currentx
            tracey = radius*math.sin(math.radians(x)) - currenty

            tracesx[i].append(tracex)
            tracesy[i].append(tracey)
            # ax.plot(tracex, tracey, color=color, label=name)
            # print(tracesx[i])
        # plt.plot(posx, posy, linewidth=0.25, color="black", )
        
        print(frame)
        # print(traces)


    planets = [ #Major axis, eccentricity, period, name, color, tracex, tracey
        [0.000,   0.00, 0.001,  "Sun",     "yellow",   [], []],
        [0.387,   0.21, 0.241,  "Mercury", "grey",     [], []],
        [0.723,   0.01, 0.615,  "Venus",   "#f5c753",  [], []],
        [1.000,   0.02, 1.000,  "Earth",   "blue",     [], []],
        [1.523,   0.09, 1.881,  "Mars",    "red",      [], []],
        # [5.202,   0.05, 11.861, "Juipter", "#f5e253",  [], []],
        # [9.576,   0.06, 29.628, "Saturn",  "orange",   [], []],
        # [19.293,  0.05, 84.747, "Uranus",  "lightblue",[], []],
        # [30.246,  0.01, 166.344,"Neptune", "blue",     [], []],
        # [39.509,  0.25, 248.348,"Pluto",   "peru",     [], []],
    ]


    center = 2 #The planet at the center
    center = planets.pop(center)

    tracesx = []
    tracesy = []
    for i in range(len(planets)): # Create a marker for every planet
        # traces.append(ax.plot([], [], label=planets[i][3], color=planets[i][4])[0]) #, "o", color=planets[i][5]))
        # print(traces)
        tracesx.append([])
        tracesy.append([])
        # print(traces[i].get_xdata())
    # print(traces)



    ax.set_title("Task 7")

    ax.set(xlabel="X/AU", ylabel='y/AU')

    # plt.xlim(-3, 3)
    # plt.ylim(-3, 3)

    # ax.xlabel("x/AU")
    # ax.ylabel("y/AU")
    
    speed = 1
    samples = 1000
    for i in range(samples):
        animate(i)
        # print(i)
    # print("All traces:", traces)
    for i in range(len(planets)):
        # print(traces[i][0])
        ax.plot(tracesx[i], tracesy[i],  label=planets[i][3], color=planets[i][4])
    
    ax.legend(loc='upper left', labelspacing=0.1)
    # ani = FuncAnimation(plt.gcf(), animate, interval=10)

    print(len(tracesx))

    return fig
#     plt.show()
# task7()
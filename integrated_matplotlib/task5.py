#Numeric method to compute polar angle vs orbit time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def task5():
    plt.rcParams["figure.figsize"] = [5.00, 5.00]
    fig = plt.Figure(dpi=100)
    ax = fig.add_subplot()
        
    def angle_vs_time(t ,P ,ecc ,theta0): 
        dtheta = 1 / 1000
        N = np.ceil(t[-1] / P)
        theta = np.arange(theta0,(2 * np.pi * N + theta0)+dtheta,dtheta)
        f = (1 - ecc * np.cos(theta)) ** (- 2)
        L = len(theta)
        c =  [1] + [4 if (x % 2 == 0) else 2 for x in range(L-2)] + [1]
        tt = np.multiply(P * ((1 - ecc ** 2) ** (3 / 2)) * (1 / (2 * np.pi)) * dtheta * (1 / 3),np.cumsum(np.multiply(c,f)))
        theta = interpolate.splrep(tt,theta)
        print(len(tt), len(theta), len(t))
        return theta

    # plt.plot([0,1,2,3], angle_vs_time([0,1,2,3], 248, 0.25, 0), 'o', color="red")
    plot = angle_vs_time(list(range(800)), 248, 0.25, 0)
    ax.plot(plot[0][:-4], plot[1][:-4], color="Green", label="Eccentricity=0.25")

    plot = angle_vs_time(list(range(800)), 248, 0.00, 0)
    ax.plot(plot[0][:-4], plot[1][:-4], color="Blue", label="Eccentricity=0.00")

    ax.legend(loc='upper left')
    # ax.title("Orbit Angle vs Time (Pluto)")
    ax.set(xlabel='Time (Years)', ylabel='Orbital Polar Angle (Radians)', title="Orbit Angle vs Time for pluto")
    # fig.xlabel("Time (Years)")
    # fig.ylabel("orbital polar angle (Radians)")

    # new_frame = tk.Frame(root)
    # canvas = FigureCanvasTkAgg(fig, master=new_frame)
    # canvas_widget = canvas.get_tk_widget()
    
    return fig#new_frame, canvas_widget
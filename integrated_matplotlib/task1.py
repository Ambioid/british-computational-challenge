import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import numpy as np

# plt.rcParams["figure.figsize"] = [5.00, 5.00]
# fig = plt.Figure(dpi=100)
# ax = fig.add_subplot()

# orbitalPeriod = np.array([0.241, 0.615, 1.000, 1.881, 11.861, 29.628, 84.727, 166.344, 248.348])
# semiMajorAxis = np.array([0.387, 0.723, 1.000, 1.523, 5.202, 9.576, 19.293, 30.246, 39.509])

# semiMajorAxis = np.power(semiMajorAxis, 3/2)

# plt.plot(semiMajorAxis, orbitalPeriod)
# plt.plot(semiMajorAxis, orbitalPeriod, 'o')
# plt.show()

def task1():
    
    plt.rcParams["figure.figsize"] = [5.00, 5.00]
    fig = plt.Figure(dpi=100)
    ax = fig.add_subplot()

    orbitalPeriod = np.array([0.241, 0.615, 1.000, 1.881, 11.861, 29.628, 84.727, 166.344, 248.348])
    semiMajorAxis = np.array([0.387, 0.723, 1.000, 1.523, 5.202, 9.576, 19.293, 30.246, 39.509])

    semiMajorAxis = np.power(semiMajorAxis, 3/2)

    ax.plot(semiMajorAxis, orbitalPeriod)
    ax.plot(semiMajorAxis, orbitalPeriod, 'o')    # plt.show()
    ax.set(xlabel="(a / AU)^(3/2) ", ylabel='T/Yr', title="Kepler's Third Law")
    # new_frame = tk.Frame(root)
    # canvas = FigureCanvasTkAgg(fig, master=new_frame)
    # canvas_widget = canvas.get_tk_widget()
    
    return fig#new_frame#, canvas_widget




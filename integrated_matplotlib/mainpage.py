import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.animation import FuncAnimation
import pandas as pd
import math

# def mainpage(): 

def ellipses():
    ax.cla()
    ax2.cla()
    
    
    
    global orbits, orbits3d, markers, markers_3d
    # print(len(orbits))
    orbits = []
    orbits3d = []
    
    markers = []
    for i in range(len(planets)): # Create a marker for every planet
        markers.append(ax.plot([], [],  'o', color=planets[i][6])[0])

    markers_3d = []
    for i in range(len(planets)): # Create a marker for every planet
        markers_3d.append(ax2.plot([], [], [], 'o', color=planets[i][6], )[0])
    
    for i in range(len(planets)): # Create ellipses for each planet
        orbits.append(ax.plot([], [],  'o', color=planets[i][6])[0])
        orbits3d.append(ax2.plot([], [], [], 'o', color=planets[i][6], )[0])
        
        if planets[i][0] == 1:
            tracey = []
            tracex2d = [] 
            tracex3d = [] 
            tracez3d = []
            
            
            for angle in range(1000):
                x = angle*360/999
                # x = (2*math.pi*i/9)/period
                major_axis, period, eccentricity, inclination, name, color = planets[i][1], planets[i][3], planets[i][2], planets[i][4], planets[i][5],  planets[i][6]

                radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
                
                tracey.append(radius*np.sin(math.radians(x)))
                
                # if inclination == None:
                tracex2d.append(radius*np.cos(math.radians(x)))
                
                tracex3d.append(radius*np.cos(math.radians(x))*np.cos(math.radians(inclination)))
                tracez3d.append(radius*np.cos(math.radians(x))*np.sin(math.radians(inclination)))
            
            
            orbits[i] = (ax.plot(tracex2d, tracey, label=name, color=color)[0])
            orbits3d[i] = (ax2.plot3D(tracex3d, tracey, tracez3d, label=name, color=color))
            # if inclination == None:
            
            # else:
    # print(orbits)
    ax.legend(loc='upper left')
    ax2.legend(loc='upper left')
    return orbits, orbits3d


def animate(frame):
    frame + 5
    for i in range(len(planets)):
        if planets[i][0] == 1:
            major_axis, period, eccentricity = planets[i][1], planets[i][3], planets[i][2]

            x = (2*math.pi*frame)/period

            radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
            tracex = (radius*np.cos(math.radians(x)))
            tracey = (radius*np.sin(math.radians(x)))
            
            markers[i].set_data(tracex, tracey)
        else:
            markers[i].set_data([], [])
    return markers


def animate_3d(frame):
    
    for i in range(len(planets)):
        if planets[i][0] == 1:
        
            major_axis, period, eccentricity, inclination= planets[i][1], planets[i][3], planets[i][2], planets[i][4]

            x = (2*math.pi*frame)/period

            radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
            tracex = (radius*np.cos(math.radians(x))*np.cos(math.radians(inclination)))
            tracey = (radius*np.sin(math.radians(x)))
            tracez = (radius*np.cos(math.radians(x))*np.sin(math.radians(inclination)))


            markers_3d[i].set_data(tracex, tracey)
            markers_3d[i].set_3d_properties(tracez)
        else:
            markers_3d[i].set_data([], [])
            markers_3d[i].set_3d_properties([])
    return markers_3d


speed = 1
def change_speed():
    global speed
    speed += 0.2
    
def frames_gen():
    frames = 0
    while True:
        yield frames
        frames += speed
        
rootwin = tk.Tk()
rootwin.wm_title("Homepage")

root = tk.Frame()
root.pack()


# button = tk.Button(root, text='Confirm', width=25, command=change_speed)
# button.pack(side=tk.BOTTOM)


plt.rcParams["figure.figsize"] = [5.00, 5.00]
fig = plt.Figure(dpi=100)
ax = fig.add_subplot()#xlim=(-2, 2), ylim=(-2,2))

fig2 = plt.Figure(dpi=100)
ax2 = fig2.add_subplot(projection='3d')#, xlim=(-2, 2), ylim=(-2,2), )

# ax2.set(xlabel='x/AU', zlim=(ax2.get_xlim()))
# print("Xlim:", ax2.get_xlim())
# ax2.axes(projection='3d')
# fig.tight_layout()
# fig2.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas.draw()
canvas2.draw()


# Important control stuff or something
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button = tk.Button(master=root, text="Quit", command=root.quit)
button.pack(side=tk.BOTTOM)

toolbar.pack(side=tk.BOTTOM, fill=tk.X)

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(side=tk.LEFT, anchor=tk.W)  

# Create an Entry widget for input
entry = tk.Entry(checkbox_frame)
entry.pack(padx=10, pady=10, side=tk.TOP)


canvas.get_tk_widget().pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
canvas2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

planets = [ 
       #Major axis, eccentricity, period, inclination, name, color
    [1, 0.000,    0.00,  0.001,   0.00, "Sun",     "yellow",   ],
    [1, 0.387,    0.21,  0.241,   7.00, "Mercury", "grey",   ],
    [1, 0.723,    0.01,  0.615,   3.39, "Venus",   "#f5c753", ],
    [1, 1.000,    0.02,  1.000,   0.00, "Earth",   "blue",   ],
    [1, 1.523,    0.09,  1.881,   1.85, "Mars",    "red",    ],
    [0, 2.77,     0.0785,4.603,   10.6, "Ceres",   "#b58c76" ],
    [0, 5.202,    0.05,  11.861,   1.31, "Jupiter", "#f5e253"],
    [0, 9.576,    0.06,  29.628,   2.49, "Saturn",  "orange"],
    [0, 19.293,   0.05,  84.747,  -0.77, "Uranus",  "lightblue"],
    [0, 30.246,   0.01,  166.344,  1.77, "Neptune", "blue"],
    [0, 39.509,   0.25,  248.348, -17.5, "Pluto", "peru"],
    [0, 26.092,   0.9632,133.280, 113.28, "Swift Turtle", "lightblue"],
    
    # Tau Ceti system
    [0, 0.000, 0.01, 0.00001, 0, "Tau Ceti", "yellow"],
    [0, 0.133, 0.06, 0.07547169811320755, 0, "G", "red"],
    [0, 0.243, 0.23, 0.13424657534246580, 0, "H", "Green"],
    [0, 0.538, 0.18, 0.44383561643835620, 0, "E", "lightblue"],
    [0, 1.334, 0.16, 1.74246575342465800, 0, "F", "orange"],
    
    # Proxima centauri system
    [0, 0.000, 0.01, 0.00001, 0, "Alpha Centauri", "yellow"],
    [0, 0.028, 0.04,  0.01403287671232877, 0.0, "Promixa Centarui D", "green"],
    [0, 0.048, 0.01,  0.03041095890410959, 0.0, "Proxima Centauri B", "grey"],
    [0, 1.489, 0.00,  5.20547945205479500, 133, "Proxima Centauri C", "blue"],
] 



def get_checkbox_values():
    print(len(orbits))
    # ax.clear()
    
    print(len(orbits))
    # orbits = []
    # orbits3d = []
    # for i in range(len(planets)): # Create 2d ellipses
    #     orbits.append(ellipse(planets[i][1], planets[i][2], planets[i][5], planets[i][6]))

    # for i in range(len(planets)): #Create 3d elipses
    #     orbits3d.append(ellipse(planets[i][1], planets[i][2], planets[i][5], planets[i][6], planets[i][4]))
    global speed
    speed = float(entry.get())
    
    for i, [checkbox_var, label] in enumerate(checkboxes):
        checkbox_value = checkbox_var.get()
        planets[i][0] =  checkbox_value       
        # print(f"{label}: {'Checked' if checkbox_value == 1 else 'Unchecked'}")
    ellipses()
    canvas.draw()




# Create a list of checkbox variables and labels dynamically
checkboxes = []
for i in range(len(planets)):
    checkbox_var = tk.IntVar(value=planets[i][0])
    label = f"Enable: {planets[i][5]}"
    checkboxes.append((checkbox_var, label))


# Create checkboxes dynamically
for checkbox_var, label in checkboxes:
    checkbox = tk.Checkbutton(checkbox_frame, text=label, variable=checkbox_var)
    checkbox.pack(anchor=tk.W)

# Create a button to get the checkbox values
get_value_button = tk.Button(checkbox_frame, text="Update", command=get_checkbox_values)
get_value_button.pack()




ellipses()
# for i in range(len(planets)): # Create 2d ellipses
#     orbits.append(ellipse(planets[i][1], planets[i][2], planets[i][5], planets[i][6]))

# for i in range(len(planets)): #Create 3d elipses
#     orbits3d.append(ellipse(planets[i][1], planets[i][2], planets[i][5], planets[i][6], planets[i][4]))



    # print(type(markers_3d[i]))



anim = FuncAnimation(fig,     animate,    frames=frames_gen(),  interval=50, blit=True)
anim_3d = FuncAnimation(fig2, animate_3d, frames=frames_gen(),  interval=50, blit=True)



tk.mainloop()
# return root
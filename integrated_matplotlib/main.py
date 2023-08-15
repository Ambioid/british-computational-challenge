from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import tkinter as tk
# from mainpage import mainpage
from task1 import task1
from task3v2 import *
from task4v2 import *
from task5 import task5
from task6 import task6
from task6v2 import task6v2
from task7 import task7


root = tk.Tk()
root.tk.call('tk', 'scaling', 4.0)
root.title("BPHO Challenges!! :D")

def show_frame(frame):
    global current_view
    if current_view:
        current_view.pack_forget()
    frame.pack()
    current_view = frame
    
def animate_t3(frame):    
    for i in range(len(planets)):

        major_axis, period, eccentricity, name, color,= planets[i][0], planets[i][2], planets[i][1], planets[i][3], planets[i][4]

        x = (12*math.pi*frame)/period

        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
        tracex = (radius*np.cos(math.radians(x)))
        tracey = (radius*np.sin(math.radians(x)))
        
        markers[i].set_data(tracex, tracey)
    return markers

def animate_t4(frame):
    for i in range(len(planets)):
        major_axis, period, eccentricity, inclination, name, color,= planets[i][0], planets[i][2], planets[i][1], planets[i][3], planets[i][4], planets[i][5]

        x = (2*math.pi*frame*100)/period

        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
        tracex = (radius*np.cos(math.radians(x))*np.cos(math.radians(inclination)))
        tracey = (radius*np.sin(math.radians(x)))
        tracez = (radius*np.cos(math.radians(x))*np.sin(math.radians(inclination)))


        markers_3d[i].set_data(tracex, tracey)
        markers_3d[i].set_3d_properties(tracez)
    # print(frame)
    return markers_3d
planets = [ #Major axis, eccentricity, period, inclination, name, color
    [0.00,  0.00, 0.001,  0.00, "Sun",     "yellow"],
    [0.387, 0.21, 0.241,  7.00, "Mercury", "grey",   ],
    [0.723, 0.01, 0.615,  3.39, "Venus",   "#f5c753", ],
    [1.000, 0.02, 1.000,  0.00, "Earth",   "blue",   ],
    [1.523, 0.09, 1.881,  1.85, "Mars",    "red",    ],
    [5.202,   0.05, 11.861,  1.31, "Jupiter", "#f5e253"],
    [9.576,   0.06, 29.628,  2.49, "Saturn",  "orange"],
    [19.293,  0.05, 84.747,  0.77, "Uranus",  "lightblue"],
    [30.246,  0.01, 166.344, 1.77, "Neptune", "blue"],
    [39.509,  0.25, 248.348, 17.5, "Pluto", "peru"],
] 
# fig1 = draw()
# canvas = FigureCanvasTkAgg(fig1, master=view2)
# canvas_widget = canvas.get_tk_widget()
# canvas_widget.pack()

select_menu = tk.Frame(root)
select_menu.pack(side=tk.TOP, anchor=tk.W)  

frame_buttons = []
def new_frame(label, fig):
    new_frame = tk.Frame(root)
    
    # print(type(new_frame), type(canvas_widget))    
    canvas = FigureCanvasTkAgg(fig, master=new_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    button = tk.Button(select_menu, text=label, command=lambda: show_frame(new_frame))
    button.pack(padx=5, pady=5, side=tk.LEFT)
    
# new_frame = tk.Frame(root)

frame_labels = ["Frame 1", "Frame 2", "Frame 3"]  # Add more labels as needed

print(frame_labels)
new_frame("Fig 1", task1())
new_frame("Fig 2", task3()[0])


fig3, ax3 = task3()
new_frame("Fig 3", fig3)
markers = []
for i in range(len(planets)): # Create a marker for every planet
    markers.append(ax3.plot([], [],  'o', color=planets[i][5])[0]) #, "o", color=planets[i][5]))
ani3 = FuncAnimation(plt.gcf(), animate_t3, interval=1)


fig4, ax4 = task4()
new_frame("Fig 4", fig4)
markers_3d = []
for i in range(len(planets)): # Create a marker for every planet
    markers_3d.append(ax4.plot([], [], [], 'o', color=planets[i][5])[0])
ani4 = FuncAnimation(plt.gcf(), animate_t4, interval=1)

new_frame("Fig 5", task5())

new_frame("Fig 6", task6v2())

new_frame("Fig 7", task7())

# Initialize the current view
current_view = None

root.mainloop()

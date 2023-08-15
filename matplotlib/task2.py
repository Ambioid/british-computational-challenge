import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count


def ellipse(major_axis, eccentricity, period, name, color):
    tracex = [] 
    tracey = []

    for i in range(1000):
        # the = i*360/999
        x = (2*math.pi*i/9)/period

        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
        tracex.append(radius*np.cos(math.radians(x)))
        tracey.append(radius*np.sin(math.radians(x)))
        print(x)
    
    plt.plot(tracex, tracey, label=name, color=color)
    # return go.Scatter(x=tracex, y=tracey, name=name, line=dict(width=2, color=color))


orbits = [ellipse(0.387,  0.21, 0.241, "Mercury", "grey"),
          ellipse(0.723,  0.01, 0.615, "Venus",   "yellow"),
          ellipse(1.000,  0.02, 1.000, "Earth",   "blue"),
          ellipse(1.523,  0.09, 1.881, "Mars",    "red"),
          ]
# orbits = [ellipse(5.202,   0.05, 11.861, "Juipter", "yellow"),
#           ellipse(9.576,   0.06, 29.628, "Saturn",  "orange"),
#           ellipse(19.293,  0.05, 84.747, "Uranus",  "lightblue"),
#           ellipse(30.246,  0.01, 166.344,"Neptune", "blue"),
#           ellipse(39.509,  0.25, 248.348,"Pluto", "peru"),
#           ]

# Copy paste the data again using list comprehension to remove the legend visibility
# orbits +=(go.Scatter(x=orbits[i].x, y=orbits[i].y, showlegend=False, line=dict(width=2, color=orbits[i].line["color"])) for i in range(len(orbits)))

plt.xlabel("x/AU")
plt.ylabel("y/AU")
plt.grid()
plt.show()

"""
fig = go.Figure(data=orbits,
                     
    layout=go.Layout(
        title_text="Animation test", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None,{"frame": {"duration": 0.5, 
                                                              "redraw": False},
                                                              "fromcurrent": False, 
                                                              "transition": {"duration": 0}}])])]),
    frames=[go.Frame(
        data=[

            go.Scatter(
            x=[orbits[i].x[k]],
            y=[orbits[i].y[k]],
            mode="markers",
            marker=dict(color=orbits[i].line["color"], size=20)) for i in range(len(orbits)//2, len(orbits))
            ])
        for k in range(1000)]
)

# plotly.offline.plot(figB, auto_play = False)
js = '''document.body.style.backgroundColor = "#000";'''

fig.show(renderer="browser",post_script=[js])
"""







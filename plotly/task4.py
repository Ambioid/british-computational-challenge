import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math


def ellipse(name, major_axis, eccentricity, period, inclination, color):
    tracex = [] 
    tracey = []
    tracez = []
    
    timesteps = 1000
    

    for i in range(timesteps):
        # the = i*360/999
        x = (2*math.pi*i/9)/period

        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
        tracex.append(radius*np.cos(math.radians(x)))
        tracey.append(radius*np.sin(math.radians(x)))

        tracez.append(tracex[-1]*np.sin(math.radians(inclination)))
        tracex[-1] = tracex[-1] *np.cos(math.radians(inclination))
    
    print(math.radians(inclination))
    return go.Scatter3d(x=tracex, y=tracey, z=tracez, name=name, marker=dict(size=0.1), line=dict(width=2, color=color))


orbits = [ellipse("Mercury", 0.387,  0.21, 0.241, 7.00, "grey"),
          ellipse("Venus",   0.723,  0.01, 0.615, 3.39, "yellow"),
          ellipse("Earth",   1.000,  0.02, 1.000, 0.00, "blue"),
          ellipse("Mars",    1.523,  0.09, 1.881, 1.85, "red"),
          ] 
# orbits = [ellipse(5.202,   0.05, 11.861, "Juipter" , "yellow"),
#           ellipse(9.576,   0.06, 29.628, "Saturn",   "orange"),
#           ellipse(19.293,  0.05, 84.747, "Uranus",   "lightblue"),
#           ellipse(30.246,  0.01, 166.344,"Neptune" , "blue"),
#           ellipse(39.509,  0.25, 248.348,"Pluto",  "peru"),
#           ]

# Copy paste the data again using list comprehension to remove the legend visibility
orbits +=(go.Scatter3d(x=orbits[i].x, y=orbits[i].y, z=orbits[i].z, showlegend=False, marker=dict(size=0.1), line=dict(width=2, color=orbits[i].line["color"])) for i in range(len(orbits)))

fig = go.Figure(data=orbits,
                     
    layout=go.Layout(
        title_text="Animation test", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None,{"frame": {"duration": 0.5, 
                                                              "redraw": False},
                                                              "fromcurrent": False, 
                                                              "transition": {"duration": 0}}])])],
                                                              ),
    
    
    
    frames=[go.Frame(
        data=[

            go.Scatter3d(
            x=[orbits[i].x[k]],
            y=[orbits[i].y[k]],
            z=[orbits[i].z[k]],
            mode="markers",

            marker=dict(color=orbits[i].line["color"], size=5))  # Iterate through all the orbits and apply their color
            for i in range(len(orbits)//2, len(orbits))
            ])
        for k in range(1000)]
)

# plotly.offline.plot(figB, auto_play = False)
# js = '''document.body.style.backgroundColor = "#000";'''

# fig.show(renderer="browser",post_script=[js])
fig.show()

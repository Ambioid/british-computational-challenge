import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math

major_axis = 0.387
eccentricity = 0.21
def ellipse(major_axis, eccentricity, name):
    tracex = [] 
    tracey = []
    for i in range(1000):
        x = i*360/999
        radius = (major_axis*(1-(eccentricity**2)))/(1-(eccentricity*np.cos(math.radians(x))))
        tracex.append(radius*np.cos(math.radians(x)))
        tracey.append(radius*np.sin(math.radians(x)))
        print(x)
    
    df = pd.DataFrame(dict(
    x = tracex,
    y = tracey
    ))
    return go.Scatter(x=tracex, y=tracey, name=name)

# graph = ellipse(0.387,  0.21)
# fig = px.line(ellipse(0.387,  0.21), x="x", y="y", title="Sorted Input") 
# graph = ellipse(0.723,  0.01)
# fig.add_scatter(x=graph["x"], y=graph["y"])

fig = go.Figure()

fig.add_trace(ellipse(0.387,  0.21, "Mercury")) 
fig.add_trace(ellipse(0.723,  0.01, "Venus")) 

fig.show()

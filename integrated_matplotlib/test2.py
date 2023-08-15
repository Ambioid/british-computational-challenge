import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def generate_graph():
    fig = Figure(figsize=(4, 3), dpi=100)
    ax = fig.add_subplot(111)
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title("Matplotlib Graph")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    return fig

def embed_graph(frame):
    fig = generate_graph()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def show_frame(frame):
    global current_frame
    if current_frame:
        current_frame.pack_forget()
    frame.pack()
    current_frame = frame

def create_frame_with_graph(root, label):
    new_frame = ttk.Frame(root)
    embed_graph(new_frame)
    button = ttk.Button(root, text=label, command=lambda: show_frame(new_frame))
    button.pack(padx=5, pady=5, side=tk.LEFT)
    return new_frame

root = tk.Tk()
root.title("Toggle Matplotlib Graph Frames")

frame_labels = ["Frame 1", "Frame 2", "Frame 3", "Frame 4"]  # Add more labels as needed

frame_list = []
for label in frame_labels:
    frame = create_frame_with_graph(root, label)
    frame_list.append(frame)

# Create your own frames with custom content
custom_frame1 = ttk.Frame(root)
custom_label1 = tk.Label(custom_frame1, text="Custom Frame 1 Content")
custom_label1.pack()
frame_list.append(custom_frame1)

custom_frame2 = ttk.Frame(root)
custom_label2 = tk.Label(custom_frame2, text="Custom Frame 2 Content")
custom_label2.pack()
frame_list.append(custom_frame2)

current_frame = None  # To keep track of the current frame

root.mainloop()

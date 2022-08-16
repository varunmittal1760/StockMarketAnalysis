from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from  pandas_datareader import  data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.figure import Figure
from yahoo_fin import stock_info
from tkinter import *

root=Tk()



container = Frame(root, width=1800, height=400)
container.place(x=50,y=520)
container.pack_propagate(0)
        # Add a text widget
text=Text(container, font=("Georgia, 24"))

text.insert(INSERT,"Varun")

root.mainloop()
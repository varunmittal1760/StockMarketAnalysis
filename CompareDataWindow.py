from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from  pandas_datareader import  data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.figure import Figure
from yahoo_fin import stock_info
from tkinter import *
from pandas.plotting import scatter_matrix
import pandas as pd

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class CompareDataWindow:
    global vr1
    global vr2





    def loadMultipleGraph(self):

        start = datetime.today() - timedelta(days=int(5))
        end = datetime.today()
        print(vr1.get(),vr2.get())

        #if(vr1.get()==1):
        tcsDataset = data.DataReader("tcs.bo", 'yahoo',start ,end )
        tcsDataset['Open'].plot(label="tcs", figsize=(6, 4))
        #if(var4.get()==1):
            #hclDataset = data.DataReader("hcltech.bo", 'yahoo', start, end)
            #hclDataset['Open'].plot(label="hcl", figsize=(6, 4))
        #if(vr2.get()==1):
        wiproDataset = data.DataReader("wipro.bo", 'yahoo', start, end)
        wiproDataset['Open'].plot(label="wipro", figsize=(6, 4))
        plt.title('Stock Data')
        plt.legend()
        plt.show()


    def compareData(self):

        global vr1
        global vr2
        global vr4
        win = Tk()
        win.geometry('2200x2200')
        win.title("New Tab")

        l1 = Label(win, text="Stock Market Data Analysis Application", font=('times new roman', 30, 'bold'),
                   pady=2, bd=5, bg="light blue", fg="Black", relief=GROOVE)
        l1.pack(fill='x')

        cdw1=CompareDataWindow()


        # Create a tab control that manages multiple tabs
        #tabsystem = ttk.Notebook(win)

        # Create new tabs using Frame widget
        #tab1 = Frame(tabsystem)

        #tabsystem.add(tab1, text='First Tab')

        #tabsystem.pack()

        #label = Label(tab1)
        vr1 = IntVar()
        Checkbutton(win, text='TATA CONSULTANCY SERVICES', variable=vr1,onvalue=1,offvalue=0).place(x=50,y=100)
        vr2 = IntVar()
        Checkbutton(win, text='WIPRO', variable=vr2,onvalue=1,offvalue=0).place(x=50,y=130)

        var3 = IntVar()
        Checkbutton(win, text='INFOSYS', variable=var3).place(x=50,y=160)
        var4 = IntVar()
        Checkbutton(win, text='HINDUSTAN TECHNOLOGIES LIMITED', variable=var4).place(x=50,y=220)
        var5 = IntVar()
        Checkbutton(win, text='REDINGTON', variable=var5).place(x=50,y=250)
        var6 = IntVar()
        Checkbutton(win, text='Tech Mahindra', variable=var6).place(x=50,y=280)
        var7 = IntVar()
        Checkbutton(win, text='Larsen & Toubro Infotech', variable=var7).place(x=50,y=310)
        var8 = IntVar()
        Checkbutton(win, text='Mphasis Ltd', variable=var8).place(x=50,y=340)
        var9 = IntVar()
        Checkbutton(win, text='Mindtree Limited', variable=var9).place(x=50,y=370)
        var10 = IntVar()
        Checkbutton(win, text='Reliance Industries', variable=var10).place(x=50,y=190)
        var11 = IntVar()
        Checkbutton(win, text='HDFC BANK', variable=var11).place(x=500, y=100)
        var12 = IntVar()
        Checkbutton(win, text='ICICI BANK', variable=var12).place(x=500, y=130)
        var13 = IntVar()
        Checkbutton(win, text='STATE BANK OF INDIA', variable=var13).place(x=500, y=160)
        var14 = IntVar()
        Checkbutton(win, text='LIC INDIA', variable=var14).place(x=500, y=220)
        var15 = IntVar()
        Checkbutton(win, text='BHARTI AIRTEL', variable=var15).place(x=500, y=250)
        var16 = IntVar()
        Checkbutton(win, text='BAJAJ FINANCE', variable=var16).place(x=500, y=280)
        var17 = IntVar()
        Checkbutton(win, text='ITC LIMITED', variable=var17).place(x=500, y=310)
        var18 = IntVar()
        Checkbutton(win, text='KOTAK MAHINDRA', variable=var18).place(x=500, y=340)
        var19 = IntVar()
        Checkbutton(win, text='MARUTI SUZUKI INDIA', variable=var19).place(x=500, y=370)
        var20 = IntVar()
        Checkbutton(win, text='AXIS BANK', variable=var20).place(x=500, y=190)

        button6 = Button(win, pady=10, text="Comparison", command=cdw1.loadMultipleGraph, font='Arial 10 bold',
                         bg="light blue")
        button6.place(x=50, y=480)

        button7 = Button(win, pady=10, text="Back", command=win.destroy, font='Arial 10 bold',
                         bg="light blue")
        button7.place(x=200, y=480)

        '''label.grid(column=1,
                   row=1,
                   padx=40,
                   pady=40)'''




        global graphtype
        graphtype=StringVar()


        l5=Label(win,text='Graph Type:',font=("Arial", 14))
        l5.place(x=50,y=420)
        graphchoosen = ttk.Combobox(win, width=27, textvariable=graphtype)
        graphchoosen['values'] = ('Open',
                                 'Close',
                                 'Volume',
                                 'Total Traded',
                                 'Moving Average',
                                 'Scatter Matrix',
                                 'Candle Stick',
                                 'Histogram',
                                 'Box Plot',
                                 'Cumulative Return',
                                  )
        graphchoosen.current(0)
        graphchoosen.place(x=220, y=420)

        win.mainloop()



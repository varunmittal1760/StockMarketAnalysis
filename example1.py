from tkinter import *
from tkinter import ttk

class twobutton:

    global vr1
    global vr2

    def loadMultipleGraph(self):

        print(vr1.get(), vr2.get())
    def checktwobutton(self):
        global vr1
        global vr2
        win=Tk()
        win.geometry('2000x2000')
        vr1 = IntVar()
        abc1=twobutton()
        Checkbutton(win, text='TATA CONSULTANCY SERVICES', variable=vr1, onvalue=1, offvalue=0).place(x=50, y=100)
        vr2 = IntVar()
        Checkbutton(win, text='WIPRO', variable=vr2, onvalue=1, offvalue=0).place(x=50, y=130)
        button6 = Button(win, pady=10, text="Comparison", command=abc1.loadMultipleGraph, font='Arial 10 bold',
                                 bg="light blue")
        button6.place(x=50, y=480)

        win.mainloop()

ac1=twobutton()
ac1.checktwobutton()
from tkinter import *

from tkinter import ttk


class GraphTabbedWindow:
    def tabs(self):
        win = Tk()
        win.title("New Tab")

        # Create a tab control that manages multiple tabs
        tabsystem = ttk.Notebook(win)

        # Create new tabs using Frame widget
        tab1 = Frame(tabsystem)
        tab2 = Frame(tabsystem)
        tab3 = Frame(tabsystem)
        tab4 = Frame(tabsystem)
        tab5 = Frame(tabsystem)
        tab6 = Frame(tabsystem)
        tab7 = Frame(tabsystem)
        tab8 = Frame(tabsystem)

        tabsystem.add(tab1, text='First Tab')
        tabsystem.add(tab2, text='Second Tab')
        tabsystem.add(tab3, text='Third Tab')
        tabsystem.add(tab4, text='Fourth Tab')
        tabsystem.add(tab5, text='Fifth Tab')
        tabsystem.add(tab6, text='Sixth Tab')
        tabsystem.add(tab7, text='Seventh Tab')
        tabsystem.add(tab8, text='Eigth Tab')

        tabsystem.pack(expand=1, fill="both")

        label = Label(tab1, text="New Tab")

        label.grid(column=1,
                   row=1,
                   padx=40,
                   pady=40)
        label2nd = Label(tab2, text="Now we are able to see another tab")
        label2nd.grid(column=1,
                      row=1,
                      padx=40,
                      pady=40)
        label3rd = Label(tab3, text="Now we are able to see another tab")
        label3rd.grid(column=1,
                      row=1,
                      padx=40,
                      pady=40)
        label4th = Label(tab4, text="Now we are able to see another tab")
        label4th.grid(column=1,
                      row=1,
                      padx=40,
                      pady=40)
        label5th = Label(tab5, text="Now we are able to see another tab")
        label5th.grid(column=1,
                      row=1,
                      padx=40,
                      pady=40)
        label6th = Label(tab6, text="Now we are able to see another tab")
        label6th.grid(column=1,
                      row=1,
                      padx=40,
                      pady=40)
        label7th = Label(tab7, text="Now we are able to see another tab")
        label7th.grid(column=1,
                      row=1,
                      padx=40,
                      pady=40)
        label8th = Label(tab8, text="Now we are able to see another tab")
        label8th.grid(column=1,
                      row=1,
                      padx=40,
                      pady=40)

        win.mainloop()
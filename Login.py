from tkinter import *

from tkinter import ttk

import mysql.connector

from StockMarketAnalysis.Window import GraphTabbedWindow
from StockMarketAnalysis.StockMarketApplication import MainWindow

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
root = Tk()
def loginForm():

    root.geometry("1000x500")

    global login
    global password
    login = StringVar()
    password = StringVar()

    root.title("Stock Market Data Analysis Login Page")
    Label(text="Welcome to Login Page", bg="yellow", width="30", height="5", font=("Calibri", 16)).grid(row=0, column=2)

    # Defining the first row

    Label(root, text="Username -", pady=40, padx=20, font=("Calibri", 13)).grid(row=2)
    Entry(root, textvariable=login, width=35).grid(row=2, column=2)

    Label(root, text="Password -", padx=20, pady=40, font=("Calibri", 13)).grid(row=3)
    Entry(root, textvariable=password, show='*', width=35).grid(row=3, column=2)

    submitbtn = Button(root, text="Login", bg='green', font=("Calibri", 13), command=verifyCredential).grid(row=5)

    root.mainloop()




def verifyCredential():


    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="varun155",
    database="varun"
    )
    mycursor=mydb.cursor()
    sql="select * from Page where login='"+login.get()+"'and password='"+password.get()+"'"


    mycursor.execute(sql)
    count=0
    for x in mycursor:
        count=count+1
    if(count!=0):
        mainWindow= MainWindow()
        mainWindow.mainWin();

    else:
        Label(root, text="Wrong details", fg="red", width="10", height="2").grid(row=8)

    mydb.commit()



loginForm()

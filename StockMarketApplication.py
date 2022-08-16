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

global var1
global var2
global var3
global var4
global var5
global var6
global var7
global var8
global var9
global var10
global var11
global var12
global var13
global var14
global var15
global var16
global var17
global var18
global var19
global var20
global text

class MainWindow:

    def refreshStockPrice(self):
        b1.set("TCS\n"+str(format(stock_info.get_live_price("tcs.bo"),'.2f')))
        b2.set("Infosy\n"+str(format(stock_info.get_live_price("infy.bo"),'.2f')))
        b3.set("HTL\n"+str(format(stock_info.get_live_price("HCLTECH.bo"),'.2f')))
        b4.set("Redington\n"+str(format(stock_info.get_live_price("redington.bo"),'.2f')))
        b5.set("Mahindra\n"+str(format(stock_info.get_live_price("techm.bo"),'.2f')))
        b6.set("Larsen\n"+str(format(stock_info.get_live_price("lti.bo"),'.2f')))
        b7.set("Mphasis\n"+str(format(stock_info.get_live_price("Mphasis.bo"),'.2f')))
        b8.set("Mindtree\n"+str(format(stock_info.get_live_price("mindtree.bo"),'.2f')))
        b9.set("Reliance\n"+str(format(stock_info.get_live_price("reliance.bo"),'.2f')))
        b10.set("HDFC\n"+str(format(stock_info.get_live_price("hdfcbank.bo"),'.2f')))
        b11.set("ICICI\n"+str(format(stock_info.get_live_price("icicibank.bo"),'.2f')))
        b12.set("SBI\n"+str(format(stock_info.get_live_price("sbin.bo"),'.2f')))
        b13.set("LIC\n"+str(format(stock_info.get_live_price("lici.bo"),'.2f')))
        b14.set("Airtel\n"+str(format(stock_info.get_live_price("bhartiartl.bo"),'.2f')))
        b15.set("Bajaj\n"+str(format(stock_info.get_live_price("bajfinance.bo"),'.2f')))
        b16.set("ITC\n"+str(format(stock_info.get_live_price("itc.bo"),'.2f')))
        b17.set("Kotak\n"+str(format(stock_info.get_live_price("kotakbank.bo"),'.2f')))
        b18.set("Maruti\n"+str(format(stock_info.get_live_price("maruti.bo"),'.2f')))
        b19.set("Axis\n"+ str(format(stock_info.get_live_price("axisbank.bo"),'.2f')))
        b20.set("Wipro\n"+str(format(stock_info.get_live_price("wipro.bo"),'.2f')))


    def stock_price(self):

        try:
            price = stock_info.get_live_price(code.get())
            if price!="":
                liveStocktext = "Stock Value of " + code.get() + " is " + str(format((price),'.2f'))
        except:
            liveStocktext="No data found "+code.get()

        Current_stock.set(liveStocktext)

    def getPrice(self):
        print("run successfully")


    def dataORgraph(self):

        mw2=MainWindow()
        mw2.loadData()
        mw2.loadGraph()


    def loadGraph(self):


        bankquotes = {
            "TATA CONSULTANCY SERVICES": "TCS.BO",
            "WIPRO": "WIPRO.BO",
            "INFOSYS": "INFY.BO",
            "HINDUSTAN TECHNOLOGIES LIMITED": "HCLTECH.BO",
            "REDINGTON INDIA LIMITED": "REDINGTON.BO",
            "Tech Mahindra Ltd": "TECHM.BO",
            "Larsen & Toubro Infotech Limited": "LTI.BO",
            "Mphasis Ltd": "MPHASIS.BO",
            "Mindtree Limited": "MINDTREE.BO",
            "Reliance Industries Limited": "RELIANCE.BO",
            "HDFC BANK":"HDFCBANK.BO",
            "ICICI BANK":"ICICIBANK.BO",
            "STATE BANK OF INDIA":"SBIN.BO",
            "LIC INDIA":"LICI.BO",
            "BHARTI AIRTEL":"BHARTIARTL.BO",
            "BAJAJ FINANCE":"BAJFINANCE.BO",
            "ITC LIMITED":"ITC.BO",
            "KOTAK MAHINDRA":"KOTAKBANK.BO",
            "MARUTI SUZUKI INDIA":"MARUTI.BO",
            "AXIS BANK":"AXISBANK.BO"
        }
        bankcode = bankquotes[bank.get()]
        print(bank.get(), info.get(), days.get())
        mw5=MainWindow
        start = datetime.today() - timedelta(days=int(days.get()))
        end = datetime.today()

        dataset = data.DataReader(bankcode, 'yahoo', start, end)
        type=datachoose.get()
        graphselected=graphtype.get()
        dataset['returns'] = (dataset[type] / dataset[type].shift(1)) - 1
        if graphselected=="Histogram":
            dataset['returns'].hist(bins=100, label=bankcode, alpha=0.5, figsize=(6, 4))
        if graphselected=="Open":
            dataset[type].plot(label=bankcode,figsize=(6, 4))
        if graphselected=="Close":
            dataset[type].plot(label=bankcode, figsize=(6, 4))
        if graphselected=="Volume":
            dataset[type].plot(label=bankcode,figsize=(6,4))
        if graphselected=="Total Traded":
            dataset[type].plot(label=bankcode,figsize=(6,4))
        if graphselected=="Scatter Matrix":
            scatter_matrix(dataset,figsize=(6,4))
        if graphselected=="Box Plot":
            box_df=pd.concat([dataset['returns']],axis=1)
            box_df.columns=['Dataset']
            box_df.plot(kind='box',figsize=(6,4))

        #if graphselected=="Moving Average":
            #dataset['CLose'].plot(label=bankcode,figsize=(16,5))
            #dataset['Moving Average for 60 days']=dataset['Close'].rolling(60).mean()
            #dataset['Moving Average for 60 days'].plot(label='Moving Average for 60 days')



        #dataset['Volume'].plot(label=bankcode, figsize=(15, 7))

        plt.title('Stock Data')
        plt.legend()
        plt.show()



    def loadData(self):
        bankquotes={
            "TATA CONSULTANCY SERVICES":"TCS.BO",
            "WIPRO":"WIPRO.BO",
            "INFOSYS":"INFY.BO",
            "HINDUSTAN TECHNOLOGIES LIMITED":"HCLTECH.BO",
            "REDINGTON INDIA LIMITED":"REDINGTON.BO",
            "Tech Mahindra Ltd":"TECHM.BO",
            "Larsen & Toubro Infotech Limited":"LTI.BO",
            "Mphasis Ltd":"MPHASIS.BO",
            "Mindtree Limited":"MINDTREE.BO",
            "Reliance Industries Limited":"RELIANCE.BO",
            "HDFC BANK": "HDFCBANK.BO",
            "ICICI BANK": "ICICIBANK.BO",
            "STATE BANK OF INDIA": "SBIN.BO",
            "LIC INDIA": "LICI.BO",
            "BHARTI AIRTEL": "BHARTIARTL.BO",
            "BAJAJ FINANCE": "BAJFINANCE.BO",
            "ITC LIMITED": "ITC.BO",
            "KOTAK MAHINDRA": "KOTAKBANK.BO",
            "MARUTI SUZUKI INDIA": "MARUTI.BO",
            "AXIS BANK": "AXISBANK.BO"

        }
        bankcode=bankquotes[bank.get()]
        print(bank.get(),info.get(),days.get())

        start=datetime.today() - timedelta(days=int(days.get()))
        end=datetime.today()


        dataset = data.DataReader(bankcode, 'yahoo', start, end)
        text.delete('1.0','end')
        text.insert('end',dataset)
        print(dataset)


    def loadMultipleGraph(self):

        start1 = datetime.today() - timedelta(days=int(5))
        end1 = datetime.today()
        #print(vr1.get(),vr2.get())
        #print("varun"+graphtype1.get()

        codemapping = {
            "vr1": "TCS.BO",
            "vr2": "WIPRO.BO",
            "vr3": "INFY.BO",
            "vr4": "HCLTECH.BO",
            "vr5": "REDINGTON.BO",
            "vr6": "TECHM.BO",
            "vr7": "LTI.BO",
            "vr8": "MPHASIS.BO",
            "vr9": "MINDTREE.BO",
            "vr10": "RELIANCE.BO",
            "vr11": "HDFCBANK.BO",
            "vr12": "ICICIBANK.BO",
            "vr13": "SBIN.BO",
            "vr14": "LICI.BO",
            "vr15": "BHARTIARTL.BO",
            "vr16": "BAJFINANCE.BO",
            "vr17": "ITC.BO",
            "vr18": "KOTAKBANK.BO",
            "vr19": "MARUTI.BO",
            "vr20": "AXISBANK.BO"

        }

        codelist=[]

        bankcode="123"
        counter=0
        codelist.clear()

        for i in (vr1,vr2,vr3,vr4,vr5,vr6,vr7,vr8,vr9,vr10,vr11,vr12,vr13,vr14,vr15,vr16,vr17,vr18,vr19,vr20):
            counter=counter+1
            if i.get()==1:
                ind="vr"+str(counter)
                codelist.append(codemapping[ind])

        graphtypeselected=graphtype1.get()
        if graphtypeselected=="Histogram":
            for j in codelist:


                dataset = data.DataReader(j, 'yahoo', start1, end1)
                dataset['returns'] = (dataset["High"] / dataset["High"].shift(1)) - 1
                dataset['returns'].hist(bins=100, label=j, alpha=0.5, figsize=(6, 4))
        if graphtypeselected=="Open":
            for j in codelist:
                dataset = data.DataReader(j, 'yahoo', start1, end1)
                dataset['Open'].plot(label=j,figsize=(6, 4))
        if graphtypeselected=="Close":
            for j in codelist:
                dataset = data.DataReader(j, 'yahoo', start1, end1)
                dataset['Close'].plot(label=j, figsize=(6, 4))
        if graphtypeselected=="Volume":
            for j in codelist:
                dataset = data.DataReader(j, 'yahoo', start1, end1)
                dataset['Volume'].plot(label=j,figsize=(6,4))
        if graphtypeselected=="Total Traded":
            for j in codelist:
                dataset = data.DataReader(j, 'yahoo', start1, end1)
                dataset['Total Traded'].plot(label=j,figsize=(6,4))
        if graphtypeselected=="Scatter Matrix":
            for j in codelist:
                dataset = data.DataReader(j, 'yahoo', start1, end1)
                scatter_matrix(dataset,figsize=(6,4))
        if graphtypeselected=="Box Plot":
            for j in codelist:
                dataset = data.DataReader(j, 'yahoo', start1, end1)
                box_df=pd.concat([dataset['returns']],axis=1)
                box_df.columns=['Dataset']
                box_df.plot(kind='box',figsize=(6,4))


        if(vr1.get()==1):

            tcsDataset = data.DataReader("tcs.bo", 'yahoo',start1 ,end1 )
            tcsDataset['Open'].plot(label="tcs", figsize=(6, 4))
        if(vr4.get()==1):
            hclDataset = data.DataReader("hcltech.bo", 'yahoo', start1, end1)
            hclDataset['Open'].plot(label="hcl", figsize=(6, 4))
        if(vr2.get()==1):
            wiproDataset = data.DataReader("wipro.bo", 'yahoo', start1, end1)
            wiproDataset['Open'].plot(label="wipro", figsize=(6, 4))
        plt.title('Stock Data')
        plt.legend()
        plt.show()






    def mainWin(self):
        root = Tk()
        global bank
        global info
        global days
        global text
        global fig
        global canvas
        global plt
        global code
        global Current_stock
        global liveStocktext
        global graphtype
        global datachoose
        global TCSprice
        global b1
        global b2
        global b3
        global b4
        global b5
        global b6
        global b7
        global b8
        global b9
        global b10
        global b11
        global b12
        global b13
        global b14
        global b15
        global b16
        global b17
        global b18
        global b19
        global b20
        global vr1
        global vr2
        global vr3
        global vr4
        global vr5
        global vr6
        global vr7
        global vr8
        global vr9
        global vr10
        global vr11
        global vr12
        global vr13
        global vr14
        global vr15
        global vr16
        global vr17
        global vr18
        global vr19
        global vr20

        bank = StringVar()
        info = IntVar()
        days = StringVar()
        code = StringVar()
        Current_stock = StringVar()
        graphtype = StringVar()
        datachoose=StringVar()
        b1 = StringVar()
        b2 = StringVar()
        b3 = StringVar()
        b4 = StringVar()
        b5 = StringVar()
        b6 = StringVar()
        b7 = StringVar()
        b8 = StringVar()
        b9 = StringVar()
        b10 = StringVar()
        b11 = StringVar()
        b12 = StringVar()
        b13 = StringVar()
        b14 = StringVar()
        b15 = StringVar()
        b16 = StringVar()
        b17 = StringVar()
        b18 = StringVar()
        b19 = StringVar()
        b20 = StringVar()

        root.state("zoomed")
        l7=Label(root, text="Stock Market Data Analysis Application", font=('times new roman', 30, 'bold'),
                      pady=2, bd=5, bg="light blue", fg="Black", relief=GROOVE)
        l7.pack(fill='x')
        mw1 = MainWindow()

        TCSprice=str(format(stock_info.get_live_price("tcs.bo"),'.2f'))
        Infosysprice=str(format(stock_info.get_live_price("infy.bo"),'.2f'))
        HTLprice=str(format(stock_info.get_live_price("HCLTECH.bo"),'.2f'))
        Redingtonprice=str(format(stock_info.get_live_price("redington.bo"),'.2f'))
        Mahindraprice = str(format(stock_info.get_live_price("techm.bo"),'.2f'))
        Larsenprice = str(format(stock_info.get_live_price("lti.bo"),'.2f'))
        Mphasisprice=str(format(stock_info.get_live_price("Mphasis.bo"),'.2f'))
        Mindtreeprice = str(format(stock_info.get_live_price("mindtree.bo"),'.2f'))
        Relianceprice = str(format(stock_info.get_live_price("reliance.bo"),'.2f'))
        HDFCprice = str(format(stock_info.get_live_price("hdfcbank.bo"),'.2f'))
        ICICIprice = str(format(stock_info.get_live_price("icicibank.bo"),'.2f'))
        SBIprice = str(format(stock_info.get_live_price("sbin.bo"),'.2f'))
        LICprice = str(format(stock_info.get_live_price("lici.bo"),'.2f'))
        Airtelprice = str(format(stock_info.get_live_price("bhartiartl.bo"),'.2f'))
        Bajajprice = str(format(stock_info.get_live_price("bajfinance.bo"),'.2f'))
        ITCprice = str(format(stock_info.get_live_price("itc.bo"),'.2f'))
        Kotakprice = str(format(stock_info.get_live_price("kotakbank.bo"),'.2f'))
        Marutiprice = str(format(stock_info.get_live_price("maruti.bo"),'.2f'))
        Axisprice =str(format(stock_info.get_live_price("axisbank.bo"),'.2f'))
        Wiproprice =str(format(stock_info.get_live_price("wipro.bo"),'.2f'))

        container2 = Frame(root, width=600, height=400, highlightbackground="black", highlightthickness=3)
        container2.place(x=20, y=70)
        container2.pack_propagate(0)
        container3 = Frame(root, width=600, height=450, highlightbackground="black", highlightthickness=3)
        container3.place(x=650, y=70)
        container3.pack_propagate(0)
        container4 = Frame(root, width=600, height=450, highlightbackground="black", highlightthickness=3)
        container4.place(x=1280, y=70)
        container4.pack_propagate(0)

        s3 = Label(container2, text="Load Data and Graph", font='Arial 17 bold')
        s3.place(x=50, y=30)

        l2=Label(root, text='Company :',font=("Arial", 14))
        l2.place(x=50,y=150)
        bankchoosen = ttk.Combobox(root, width=27,textvariable=bank)
        bankchoosen['values'] = ("TATA CONSULTANCY SERVICES",
            "WIPRO",
            "INFOSYS",
            "HINDUSTAN TECHNOLOGIES LIMITED",
            "REDINGTON INDIA LIMITED",
            "Tech Mahindra Ltd",
            "Larsen & Toubro Infotech Limited",
            "Mphasis Ltd",
            "Mindtree Limited",
            "Reliance Industries Limited",
            "HDFC BANK",
            "ICICI BANK",
            "STATE BANK OF INDIA",
            "LIC INDIA",
            "BHARTI AIRTEL",
            "BAJAJ FINANCE",
            "ITC LIMITED",
            "KOTAK MAHINDRA",
            "MARUTI SUZUKI INDIA",
            "AXIS BANK"
            )
        bankchoosen.current(0)
        bankchoosen.place(x=200,y=155)
        l3=Label(root,text='Data Type :',font=("Arial", 14))
        l3.place(x=50,y=200)
        datachoosen = ttk.Combobox(root, width=27, textvariable=datachoose)
        datachoosen['values'] = ('High',
                                 'Low',
                                 'Volume',
                                 'Adj',
                                 'Close',
                                 )
        datachoosen.current(0)
        datachoosen.place(x=200, y=205)
        l4=Label(root, text='Days :',font=("Arial", 14))
        l4.place(x=50,y=250)
        dayschoosen = ttk.Combobox(root, width=27,textvariable=days)
        dayschoosen['values'] = ('1',
                                 '5',
                                 '15',
                                 '30',
                                 '180',
                                 '365',
                                 '1825',
                                 '3650')
        dayschoosen.current(0)
        dayschoosen.place(x=200,y=250)
        print(info.get())

        l5=Label(root,text='Graph Type:',font=("Arial", 14))
        l5.place(x=50,y=300)
        graphchoosen = ttk.Combobox(root, width=27, textvariable=graphtype)
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
        graphchoosen.place(x=200, y=305)




        button2 = Button(root, pady=10, text="Load Stock Data", command=mw1.dataORgraph,font='Arial 10 bold',bg="light blue")
        button2.place(x=50,y=350)
        button3=Button(root,pady=10,text="Comparison",command=mw1.loadMultipleGraph,bg="light blue",font='Arial 10 bold')
        button3.place(x=1100,y=460)

        result2 = Label(root, text="", textvariable=Current_stock,font='Arial 10 bold')
        result2.place(x=700,y=200)

        s5 = Label(root, text="Comparison Stocks ", font='Arial 17 bold')
        s5.place(x=700, y=90)

        vr1 = IntVar()
        Checkbutton(root, text='TCS', variable=vr1, onvalue=1, offvalue=0).place(x=700, y=130)
        vr2 = IntVar()
        Checkbutton(root, text='WIPRO', variable=vr2, onvalue=1, offvalue=0).place(x=700, y=160)

        vr3 = IntVar()
        Checkbutton(root, text='INFOSYS', variable=vr3).place(x=700, y=190)
        vr4 = IntVar()
        Checkbutton(root, text='HTLTECH', variable=vr4).place(x=700, y=220)
        vr5 = IntVar()
        Checkbutton(root, text='REDINGTON', variable=vr5).place(x=700, y=250)
        vr6 = IntVar()
        Checkbutton(root, text='Tech Mahindra', variable=vr6).place(x=900, y=130)
        vr7 = IntVar()
        Checkbutton(root, text='Larsen & Toubro ', variable=vr7).place(x=900, y=190)
        vr8 = IntVar()
        Checkbutton(root, text='Mphasis Ltd', variable=vr8).place(x=900, y=160)
        vr9 = IntVar()
        Checkbutton(root, text='Mindtree Limited', variable=vr9).place(x=900, y=220)
        vr10 = IntVar()
        Checkbutton(root, text='Reliance ', variable=vr10).place(x=900, y=250)
        vr11 = IntVar()
        Checkbutton(root, text='HDFC BANK', variable=vr11).place(x=700, y=280)
        vr12 = IntVar()
        Checkbutton(root, text='ICICI BANK', variable=vr12).place(x=700, y=310)
        vr13 = IntVar()
        Checkbutton(root, text='STATE BANK OF INDIA', variable=vr13).place(x=700, y=340)
        vr14 = IntVar()
        Checkbutton(root, text='LIC INDIA', variable=vr14).place(x=700, y=370)
        vr15 = IntVar()
        Checkbutton(root, text='BHARTI AIRTEL', variable=vr15).place(x=700, y=400)
        vr16 = IntVar()
        Checkbutton(root, text='BAJAJ FINANCE', variable=vr16).place(x=900, y=280)
        vr17 = IntVar()
        Checkbutton(root, text='ITC LIMITED', variable=vr17).place(x=900, y=310)
        vr18 = IntVar()
        Checkbutton(root, text='KOTAK MAHINDRA', variable=vr18).place(x=900, y=340)
        vr19 = IntVar()
        Checkbutton(root, text='MARUTI SUZUKI INDIA', variable=vr19).place(x=900, y=370)
        vr20 = IntVar()
        Checkbutton(root, text='AXIS BANK', variable=vr20).place(x=900, y=400)
        global graphtype1
        graphtype1 = StringVar()

        l8 = Label(root, text='Graph Type:', font=("Arial", 14))
        l8.place(x=700, y=430)
        graphchoosen1 = ttk.Combobox(root, width=27, textvariable=graphtype1)
        graphchoosen1['values'] = ('Open',
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
        graphchoosen1.current(0)
        graphchoosen1.place(x=900, y=430)

        s1=Label(root,text="Search Live Stocks",font='Arial 17 bold')
        s1.place(x=1310, y=410)


        e1=Entry(root,textvariable=code,width=35)
        e1.place(x=1310,y=450)
        button4=Button(root,pady=10,text="Get Live Price",command=mw1.stock_price,font='Arial 10 bold',bg="light blue")
        button4.place(x=1600,y=430)
        if (mw1.getPrice==0):
            l6=Label(root, text="Wrong details", fg="red", width="10", height="2")
            l6.place(x=1600,y=450)

        v = Scrollbar(root, orient='vertical')
        v.pack(side=RIGHT,fill='y')

        s5=Label(root,text="Data",font='Arial 17 bold')
        s5.place(x=50,y=470)

        container = Frame(root, width=1880, height=400,highlightbackground="black", highlightthickness=3)
        container.place(x=20,y=520)
        container.pack_propagate(0)
        # Add a text widget




        text=Text(container, font=("Georgia, 14"),yscrollcommand=v.set)

        text.pack(fill=BOTH)
        v.config(command=text.yview)

        s4 = Label(root, text="Live Price", font='Arial 17 bold')
        s4.place(x=1310, y=90)
        photo = PhotoImage(file=r"refresh2.png")

        refreshbutton=Button(root,image=photo,height=50,width=50,command=mw1.refreshStockPrice)
        refreshbutton.place(x=1520,y=80)
        print(TCSprice)
        bl1=Label(root,textvariable=b1, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b1.set("TCS\n"+TCSprice)
        #b1 = Button(root, text='TCS\n'+TCSprice, fg='black', bg='light blue',
                         #command=mw1.getPrice, height=4, width=15)
        bl1.place(x=1420,y=150)

        bl2 = Label(root, textvariable=b2, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b2.set("Wipro\n"+Wiproprice)
        bl2.place(x=1420, y=210)

        bl3 = Label(root, textvariable=b3, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b3.set('Infosys\n'+Infosysprice)
        bl3.place(x=1420, y=270)

        bl4 = Label(root, textvariable=b4, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b4.set('HTL\n'+HTLprice)
        bl4.place(x=1520, y=150)

        bl5 = Label(root, textvariable=b5 ,fg='black', bg='light blue',height=3, width=13,borderwidth=1,relief="solid")
        b5.set('Redington\n'+Redingtonprice)
        bl5.place(x=1520, y=210)

        bl6 = Label(root, textvariable=b6, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b6.set('Tech\nMahindra\n'+Mahindraprice)
        bl6.place(x=1520, y=270)

        bl7 = Label(root, textvariable=b7, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b7.set('LTI\n'+Larsenprice)
        bl7.place(x=1620, y=150)

        bl8 = Label(root, textvariable=b8, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b8.set('Mphasis\n'+Mphasisprice)
        bl8.place(x=1620, y=210)

        bl9 = Label(root, textvariable=b9, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b9.set('Mindtree\n'+Mindtreeprice)
        bl9.place(x=1620, y=270)
        bl10 = Label(root, textvariable=b10, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b10.set('HDFC BANK\n'+HDFCprice)
        bl10.place(x=1720, y=330)
        bl11 = Label(root, textvariable=b11, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b11.set('ICICI BANK\n'+ICICIprice)
        bl11.place(x=1420, y=330)
        bl12 = Label(root, textvariable=b12, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b12.set('SBI\n'+SBIprice)
        bl12.place(x=1520, y=330)
        bl13 = Label(root, textvariable=b13, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b13.set('LIC INDIA\n'+LICprice)
        bl13.place(x=1720, y=150)
        bl14 = Label(root, textvariable=b14, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b14.set('BHARTI AIRTEL\n'+Airtelprice)
        bl14.place(x=1720, y=210)
        bl15 = Label(root,textvariable=b15, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b15.set('BAJAJ\n'+Bajajprice)
        bl15.place(x=1720, y=270)
        bl16 = Label(root, textvariable=b16, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b16.set('ITC\n'+ITCprice)
        bl16.place(x=1620, y=330)
        bl17 = Label(root, textvariable=b17, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b17.set('KOTAK\nMAHINDRA\n'+Kotakprice)
        bl17.place(x=1310, y=150)
        bl18 = Label(root, textvariable=b18, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b18.set('MARUTI\n'+Marutiprice)
        bl18.place(x=1310, y=210)
        bl19 = Label(root, textvariable=b19, fg='black', bg='light blue', height=3, width=13,borderwidth=1,relief="solid")
        b19.set('Reliance\n'+Relianceprice)
        bl19.place(x=1310, y=270)
        bl20 = Label(root, textvariable=b20, fg='black', bg='light blue',height=3, width=13,borderwidth=1,relief="solid")
        b20.set('AXIS BANK\n'+Axisprice)
        bl20.place(x=1310, y=330)

        button5 = Button(root, pady=10,padx=10, text="Exit", command=root.destroy,font='Arial 10 bold',
                         bg="light blue")
        button5.place(x=930, y=930)


        root.mainloop()



mw=MainWindow()
mw.mainWin()

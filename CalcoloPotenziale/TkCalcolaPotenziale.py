from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
import pandas as pd
import pickle
from PIL import ImageTk, Image
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import learning_curve, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor

def on_closing_c():
    global finmpc
    finmpc.destroy()
    creaFinestraIniziale()

def on_closing_rn():
    global finmprn
    finmprn.destroy()
    creaFinestraIniziale()

def on_closing_lr():
    global finmplr
    finmplr.destroy()
    creaFinestraIniziale()

def mostraPotenzialeC(pot):
    global finmpc
    finmpc = Tk()  
    finmpc.geometry('404x264')  
    finmpc.title('FIFA Talent Scouting')
    finmpc.eval('tk::PlaceWindow . center')
    finmpc.iconbitmap('img/ico.ico')
    finmpc.resizable(False, False)
    if pot=="Ottima crescita >10": 
        image=Image.open("img/ottima.png")
        image= image.resize((400, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmpc, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot=="Buona crescita ]7,10]": 
        image=Image.open("img/buona.png")
        image= image.resize((400, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmpc, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot=="Normale crescita ]3,7]": 
        image=Image.open("img/normale.png")
        image= image.resize((400, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmpc, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot=="Pessima crescita <=3": 
        image=Image.open("img/pessima.png")
        image= image.resize((400, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmpc, image=carta)
        labelCarta.grid(column=0, row=0)



    finmpc.protocol("WM_DELETE_WINDOW", on_closing_c)
    #serve per mantenere aperta la finmprn
    finmpc.mainloop()

def mostraPotenzialeRN(pot):
    global finmprn
    finmprn = Tk()  
    finmprn.geometry('454x264')  
    finmprn.title('FIFA Talent Scouting')
    finmprn.eval('tk::PlaceWindow . center')
    finmprn.iconbitmap('img/ico.ico')
    finmprn.resizable(False, False)

    if pot<60:
        image=Image.open("img/min60.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==60:
        image=Image.open("img/60.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==61:
        image=Image.open("img/61.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==62:
        image=Image.open("img/62.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==63:
        image=Image.open("img/63.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==64:
        image=Image.open("img/64.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==65:
        image=Image.open("img/65.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==66:
        image=Image.open("img/66.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==67:
        image=Image.open("img/67.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==68:
        image=Image.open("img/68.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==69:
        image=Image.open("img/69.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==70:
        image=Image.open("img/70.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==71:
        image=Image.open("img/71.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==72:
        image=Image.open("img/72.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==73:
        image=Image.open("img/73.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==74:
        image=Image.open("img/74.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==75:
        image=Image.open("img/75.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==76:
        image=Image.open("img/76.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==77:
        image=Image.open("img/77.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==78:
        image=Image.open("img/78.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==79:
        image=Image.open("img/79.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==80:
        image=Image.open("img/80.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==81:
        image=Image.open("img/81.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==82:
        image=Image.open("img/82.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==83:
        image=Image.open("img/83.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==84:
        image=Image.open("img/84.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==85:
        image=Image.open("img/85.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==86:
        image=Image.open("img/86.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==87:
        image=Image.open("img/87.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==88:
        image=Image.open("img/88.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==89:
        image=Image.open("img/89.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==90:
        image=Image.open("img/90.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==91:
        image=Image.open("img/91.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==92:
        image=Image.open("img/92.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==93:
        image=Image.open("img/93.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==94:
        image=Image.open("img/94.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==95:
        image=Image.open("img/95.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==96:
        image=Image.open("img/96.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==97:
        image=Image.open("img/97.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==98:
        image=Image.open("img/98.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot>=99:
        image=Image.open("img/99.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmprn, image=carta)
        labelCarta.grid(column=0, row=0)

    finmprn.protocol("WM_DELETE_WINDOW", on_closing_rn)

    #serve per mantenere aperta la finmprn
    finmprn.mainloop()

def mostraPotenzialeLR(pot):
    print("POT= ",pot)
    global finmplr
    finmplr = Tk()  
    finmplr.geometry('454x264')  
    finmplr.title('FIFA Talent Scouting')
    finmplr.eval('tk::PlaceWindow . center')
    finmplr.iconbitmap('img/ico.ico')
    finmplr.resizable(False, False)

    if pot<60:
        image=Image.open("img/min60.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==60:
        image=Image.open("img/60.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==61:
        image=Image.open("img/61.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==62:
        image=Image.open("img/62.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==63:
        image=Image.open("img/63.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==64:
        image=Image.open("img/64.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==65:
        image=Image.open("img/65.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==66:
        image=Image.open("img/66.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==67:
        image=Image.open("img/67.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==68:
        image=Image.open("img/68.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==69:
        image=Image.open("img/69.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==70:
        image=Image.open("img/70.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==71:
        image=Image.open("img/71.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==72:
        image=Image.open("img/72.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==73:
        image=Image.open("img/73.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==74:
        image=Image.open("img/74.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==75:
        image=Image.open("img/75.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==76:
        image=Image.open("img/76.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==77:
        image=Image.open("img/77.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==78:
        image=Image.open("img/78.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==79:
        image=Image.open("img/79.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==80:
        image=Image.open("img/80.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==81:
        image=Image.open("img/81.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==82:
        image=Image.open("img/82.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==83:
        image=Image.open("img/83.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==84:
        image=Image.open("img/84.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==85:
        image=Image.open("img/85.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==86:
        image=Image.open("img/86.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==87:
        image=Image.open("img/87.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==88:
        image=Image.open("img/88.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==89:
        image=Image.open("img/89.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==90:
        image=Image.open("img/90.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==91:
        image=Image.open("img/91.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==92:
        image=Image.open("img/92.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==93:
        image=Image.open("img/93.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==94:
        image=Image.open("img/94.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==95:
        image=Image.open("img/95.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==96:
        image=Image.open("img/96.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==97:
        image=Image.open("img/97.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot==98:
        image=Image.open("img/98.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)
    elif pot>=99:
        image=Image.open("img/99.png")
        image= image.resize((450, 260), Image.ANTIALIAS)
        carta= ImageTk.PhotoImage(image)
        labelCarta= Label(finmplr, image=carta)
        labelCarta.grid(column=0, row=0)

    finmplr.protocol("WM_DELETE_WINDOW", on_closing_lr)

    #serve per mantenere aperta la finmplr
    finmplr.mainloop()

#############################   CALCOLI POTENZIALE  ##################################### 

def calcolaPotenzialeLinearRegression():
    try:
        global fincp, scaler
        eta=int(entryEta.get())
        overall=int(entryOverall.get())
        valore=int(entryValore.get())
        stipendio=int(entryStipendio.get())
        piedeDebole=int(cbPiedeDebole.get())
        skill=int(cbSkill.get())
        d = {'age': [eta], 'overall': [overall], 'value_eur': [valore], 'wage_eur': [stipendio], 'wake_foot': [piedeDebole], 'skill_moves': [skill]}
        df = pd.DataFrame(data=d)
        print(df)
        df=scaler.transform(df)
        previsione=lr_model.predict(df)
        pot=round(previsione[0])
        print(pot)
        fincp.destroy()
        mostraPotenzialeLR(pot)
    except:
        messagebox.showinfo("Errore", "Inserire i campi correttamente")


def calcolaPotenzialeRetiNeurali():
    try:
        global fincp, scaler
        eta=int(entryEta.get())
        overall=int(entryOverall.get())
        valore=int(entryValore.get())
        stipendio=int(entryStipendio.get())
        piedeDebole=int(cbPiedeDebole.get())
        skill=int(cbSkill.get())
        d = {'age': [eta], 'overall': [overall], 'value_eur': [valore], 'wage_eur': [stipendio], 'wake_foot': [piedeDebole], 'skill_moves': [skill]}
        df = pd.DataFrame(data=d)
        print(df)
        df=scaler.transform(df)
        previsione=rn_model.predict(df)
        pot=round(previsione[0])
        print(pot)
        fincp.destroy()
        mostraPotenzialeRN(pot)
    except:
        messagebox.showinfo("Errore", "Inserire i campi correttamente")


def calcolaPotenzialeClassificazione():
    try:
        global fincp
        eta=int(entryEta.get())
        overall=int(entryOverall.get())
        valore=int(entryValore.get())
        stipendio=int(entryStipendio.get())
        piedeDebole=int(cbPiedeDebole.get())
        skill=int(cbSkill.get())
        d = {'age': [eta], 'overall': [overall], 'value_eur': [valore], 'wage_eur': [stipendio], 'wake_foot': [piedeDebole], 'skill_moves': [skill]}
        df = pd.DataFrame(data=d)
        print(df)
        previsione=c_model.predict(df)
        fincp.destroy()
        mostraPotenzialeC(previsione[0])
    except:
        messagebox.showinfo("Errore", "Inserire i campi correttamente")


def creaFinestraCalcolaPotenziale(scelta):
    global fincp, entryEta, entryOverall, entryValore, entryStipendio, cbPiedeDebole, cbSkill, finprinc
    #distr
    finprinc.destroy()
    #creo una fincp 
    fincp = Tk()  
    fincp.geometry('600x207')  
    fincp.title('FIFA Talent Scouting')
    fincp.resizable(False, False)
    imagew=Image.open("img/wallp2.png")
    imagew= imagew.resize((596, 203), Image.ANTIALIAS)
    wallp= ImageTk.PhotoImage(imagew)
    labelWallp= Label(fincp, image=wallp)
    labelWallp.place(x=0, y=0)
    fincp.iconbitmap('img/ico.ico')
    #chiamo la funzione per centrare
    fincp.eval('tk::PlaceWindow . center')
    #creo font
    #myFont = Font(family="Arial Black", size=12)
    #inserisco le apposite label, le entry e il bottone per proseguire
    #labelEta=Label(fincp, text="Età",font=myFont)
    #labelEta.grid(column=0, row=0)
    entryEta=Entry(fincp)
    entryEta.grid(column=0, row=1)
    #labelOverall=Label(fincp, text="Overall",font=myFont)
    #labelOverall.grid(column=1, row=0)
    entryOverall=Entry(fincp)
    entryOverall.grid(column=1, row=1)
    #labelValore=Label(fincp, text="Valore",font=myFont)
    #labelValore.grid(column=2, row=0)
    entryValore=Entry(fincp)
    entryValore.grid(column=2, row=1)
    #labelStipendio=Label(fincp, text="Stipendio",font=myFont)
    #labelStipendio.grid(column=0, row=2)
    entryStipendio=Entry(fincp)
    entryStipendio.grid(column=0, row=3)
    #labelPiedeDebole=Label(fincp, text="Piede debole",font=myFont)
    #labelPiedeDebole.grid(column=1, row=2)
    cbPiedeDebole=ttk.Combobox(fincp,state="readonly", values=[1,2,3,4,5])
    cbPiedeDebole.grid(column=1, row=3)
    cbPiedeDebole.current(0)
    #labelSkill=Label(fincp, text="Skill",font=myFont)
    #labelSkill.grid(column=2, row=2)
    cbSkill=ttk.Combobox(fincp,state="readonly", values=[1,2,3,4,5])
    cbSkill.grid(column=2, row=3)
    cbSkill.current(0)
    if scelta==0:
        bottoneSubmit=Button(fincp, text="Calcola", command=calcolaPotenzialeLinearRegression,bg='#622b53') 
        bottoneSubmit.grid(column=1, row=4)
        imgB = PhotoImage(file="img/calcola.png")
        bottoneSubmit.config(image=imgB)
    elif scelta==1:
        bottoneSubmit=Button(fincp, text="Calcola", command=calcolaPotenzialeRetiNeurali,bg='#622b53') 
        bottoneSubmit.grid(column=1, row=4)
        imgB = PhotoImage(file="img/calcola.png")
        bottoneSubmit.config(image=imgB)
    elif scelta==2:
        bottoneSubmit=Button(fincp, text="Calcola", command=calcolaPotenzialeClassificazione,bg='#622b53') 
        bottoneSubmit.grid(column=1, row=4)
        imgB = PhotoImage(file="img/calcola.png")
        bottoneSubmit.config(image=imgB)
    #setto le grandezze minime dell righe e le colonne
    fincp.grid_columnconfigure(0, minsize=200)
    fincp.grid_columnconfigure(1, minsize=200)
    fincp.grid_columnconfigure(2, minsize=200)
    fincp.grid_rowconfigure(0, minsize=40)
    fincp.grid_rowconfigure(1, minsize=40)
    fincp.grid_rowconfigure(2, minsize=40)
    fincp.grid_rowconfigure(3, minsize=40)
    fincp.grid_rowconfigure(4, minsize=40)
    #serve per mantenere aperta la fincp
    fincp.mainloop()



def creaFinestraIniziale():
    global finprinc
    finprinc = Tk()  
    finprinc.geometry('404x398')  
    finprinc.title('FIFA Talent Scouting')
    finprinc.resizable(False, False)
    finprinc.eval('tk::PlaceWindow . center')
    imagew=Image.open("img/wallp.png")
    imagew= imagew.resize((400, 394), Image.ANTIALIAS)
    wallp= ImageTk.PhotoImage(imagew)
    labelPWallp= Label(finprinc, image=wallp)
    labelPWallp.place(x=0, y=0)
    finprinc.iconbitmap('img/ico.ico')
    bottoneLR=Button(finprinc, text="Linear Regression", command=lambda: creaFinestraCalcolaPotenziale(0),bg='#622b53') 
    bottoneLR.grid(column=0, row=1)
    imgLR = PhotoImage(file="img/lrbut.png")
    bottoneLR.config(image=imgLR)
    bottoneRN=Button(finprinc, text="Reti Neurali", command=lambda: creaFinestraCalcolaPotenziale(1),bg='#622b53') 
    bottoneRN.grid(column=0, row=2)
    imgRN = PhotoImage(file="img/rnbut.png")
    bottoneRN.config(image=imgRN)
    bottoneC=Button(finprinc, text="Classificazione", command=lambda: creaFinestraCalcolaPotenziale(2),bg='#622b53') 
    bottoneC.grid(column=0, row=3)
    imgC = PhotoImage(file="img/cbut.png")
    bottoneC.config(image=imgC)
    finprinc.grid_rowconfigure(0, minsize=150)
    finprinc.grid_rowconfigure(1, minsize=60)
    finprinc.grid_rowconfigure(2, minsize=60)
    finprinc.grid_rowconfigure(3, minsize=60)
    finprinc.grid_columnconfigure(0, minsize=398)
    #serve per mantenere aperta la finprinc
    finprinc.mainloop()

#Faccio lo scaling 
giocatori = pd.read_csv("players_20.csv" )
giocatori = giocatori.drop(giocatori[giocatori.age>25].index)
giocatori = giocatori.drop(giocatori[giocatori.overall>75].index)
giocatori=giocatori[["age","overall","potential","value_eur","wage_eur","weak_foot","skill_moves"]]
x=np.array(giocatori.drop(['potential'],1))
global scaler
scaler = preprocessing.StandardScaler().fit(x)

#carico modell9
lr_model=pickle.load(open('FifaModelLinReg.sav','rb'))
rn_model=pickle.load(open('FifaModelMLP.sav','rb'))
c_model=pickle.load(open('FifaModelRanForClas.sav','rb'))

creaFinestraIniziale()
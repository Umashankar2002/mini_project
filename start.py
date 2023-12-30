
import tkinter as tk
from tkinter import *
import pymysql
root=Tk()

root.geometry("5000x4000")
root.config(bg="pink")

def fetch():
    root.destroy()
    import fetch_data
def savedata():
    root.destroy()
    import miniproject

Button(text="registration",font="arial 15 bold",width=10,height=2,bg="yellow",command=savedata).place(x=470,y=300)

Button(text="face scane",font="arial 15 bold",width=10,height=2,bg="yellow",command=fetch).place(x=700,y=300)

root.mainloop()

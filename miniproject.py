
import tkinter as tk
from tkinter import *
import pymysql
root=Tk()
root.geometry("5000x4000")

img=PhotoImage(file="/home/apiiit-rkv/PycharmProjects/pythonProject/wallpaper2you_476102.png")
label=Label(root,image=img)
label.place(x=0,y=0,relheight=1,relwidth=1)

db = pymysql.connect(host="localhost",user="root",password="Umashankar123@",database="Student")
cursor = db.cursor()


heading=Label(text="registration form",fg="black",bg="green",width="500",height="2",font="arial 25 bold").pack()
Label(root,text="Enter your Name : ",font="arial 15 bold").place(x=300,y=150)
Label(root,text="Enter your Father Name :",font="arial 15 bold").place(x=300,y=220)
Label(root,text="Enter your Father Phone No :",font="arial 15 bold").place(x=300,y=290)
Label(root,text="Enter address :",font="arial 15 bold").place(x=300,y=360)

name=StringVar()
Father=StringVar()
phone=StringVar()
address=StringVar()
def savedata():
    firstname=name.get()
    Fathername=Father.get()
    Phonenumber=phone.get()
    Address=address.get()
    s=validate()
    if s=="u":
        x=check()
        if x=="yes":
            query = "insert into student(Name,Father,FatherNumber,address) values (%s,%s,%s,%s)"
            val = (firstname, Fathername, Phonenumber, Address)
            cursor.execute(query, val)
            db.commit()
            root.destroy()
            import face
            cursor.close()
        else:
            warin = "This number is already registred"
            warning(warin)
def check():
    b=0
    first = name.get()
    Phone = phone.get()
    q="select FatherNumber from student where FatherNumber=%s"
    v=(Phone)
    cursor.execute(q, v)
    for u in cursor:
        y=u[0]
        b=1
        c = str(y)
        k = str(Phone)
    if b==0:
        return "yes"

    elif c==k:
        return "no"

    else:
        return "yes"
def warning(war):
    Label(root,text=war,width="40",bg="red",font="arial 15 bold").place(x=460,y=550)

def validate():
    user = name.get()
    if user == "":
        warin = "name should not empty"
        warning(warin)
    elif user.isalpha():
        return validate1()
    else:
        warin = "name does't contain numbers"
        warning(warin)

def validate1():
    father = Father.get()
    if father == "":
        warin = "father name should not empty"
        warning(warin)
    elif father.isalpha():
        return validate2()
    else:
        warin = "father name does't contain numbers"
        warning(warin)

def validate2():
    phones = phone.get()
    if phones=="":
        warin = "phone number should not be empty"
        warning(warin)
    elif len(phones)!=10:
        warin = "phone number should 10 numbers"
        warning(warin)
    elif phones.isdigit():
        return validate3()
    else:
        warin = "phone number doesn't contain characters"
        warning(warin)

def validate3():
    addresses = address.get()
    if addresses=="":
        warin = "address not be empty"
        warning(warin)
    else:
        return "u"

netry=Entry(root,textvariable=name,width=30,bd=2,font=20).place(x=650,y=150)
F=Entry(root,textvariable=Father,width=30,bd=2,font=20).place(x=650,y=220)
p=Entry(root,textvariable=phone,width=30,bd=2,font=20).place(x=650,y=290)
a=Entry(root,textvariable=address,width=30,bd=2,font=20).place(x=650,y=360)


Button(text="submit",font="arial 15 bold",width=10,height=2,bg="yellow",command=savedata).place(x=600,y=450)

root.mainloop()
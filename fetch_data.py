import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from tkinter import *
import pymysql
root=Tk()
root.geometry("5000x4000")
db = pymysql.connect(host="localhost",user="root",password="Umashankar123@",database="Student")
cursor = db.cursor()


path= 'imagesattendence'
images = []
classnames=[]
mylist=os.listdir(path)
print(mylist)
for cl in mylist:
	curimg=cv2.imread(f'{path}/{cl}')
	images.append(curimg)
	classnames.append(os.path.splitext(cl)[0])
def findencodings(images):
	encodelist=[]
	for img in images:
		img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		encode=face_recognition.face_encodings(img)
		encodelist.append(encode)
	return encodelist

encodelistknown = findencodings(images)
print('encoding completed')

cap = cv2.VideoCapture(0)
i=0
while i==0:
    success, img = cap.read()
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    print("hello")
    facescurframe = face_recognition.face_locations(imgs)
    encodescurframe = face_recognition.face_encodings(imgs, facescurframe)

    for encodeface, faceloc in zip(encodescurframe, facescurframe):
        matches = face_recognition.compare_faces(encodelistknown, encodeface)
        facedis = face_recognition.face_distance(encodelistknown, encodeface)

        matchindex = np.argmin(facedis)
        i = i + 1
        if matches[matchindex]:
            name = classnames[matchindex].lower()
            print(name)
            query = "select *from student where Name=%s"
            val = (name)
            cursor.execute(query, val)
            for u in cursor:
                Label(root, text="Name of Person : ", font="arial 15 bold",bg="blue").place(x=500, y=100)
                Label(root,text=u[1], font="arial 15 bold").place(x=700, y=100)
                print("\n")
                Label(root, text="Father Name : ", font="arial 15 bold",bg="blue").place(x=500, y=200)
                Label(root,text=u[2], font="arial 15 bold").place(x=700, y=200)
                print("\n")
                Label(root, text="FatherNumber : ", font="arial 15 bold",bg="blue").place(x=500, y=300)
                Label(root,text=u[3], font="arial 15 bold").place(x=700, y=300)
                print("\n")
                Label(root, text="Address : ", font="arial 15 bold",bg="blue").place(x=500, y=400)
                Label(root,text=u[4], font="arial 15 bold").place(x=700, y=400)
            cursor.close()
        else:
            Label(root, text="not match", font="arial 15 bold", bg="blue").place(x=500, y=400)
    cv2.imshow('webcam', img)
    cv2.waitKey(1)
root.mainloop()
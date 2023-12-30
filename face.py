import cv2
import pymysql
db = pymysql.connect(host="localhost",user="root",password="Umashankar123@",database="Student")
cur = db.cursor()
i=0
if(i==0):
    vid = cv2.VideoCapture(0)
    name = input("Enter the name: ")
    if (name == ""):
        print("\nPlease enter the name\n")
        vid.release()
        cv2.destroyAllWindows()
    while (True):
        success, frame = vid.read()
        cv2.imshow(name, frame)
        cv2.imwrite("./imagesattendence/" + name + '.jpg', frame)
        print("image takenn, press 'q' to stop capturing")
        if (cv2.waitKey(1) == ord("q")):
            i=1
            break
    vid.release()
    cv2.destroyAllWindows()
if(i==1):
    import start

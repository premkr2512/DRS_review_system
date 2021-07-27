import tkinter
import PIL.Image,PIL.ImageTk
import cv2
from functools import partial #if we insert argument in the function command will not find it has argument or not
import threading
import time
#import imutils
width = 650
height = 368
w= tkinter.Tk()
w.title("DRS")
canvas = tkinter.Canvas(w,width = width,height = height)
cv_img = cv2.cvtColor(cv2.imread("Penguins.jpg"),cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_om_canvas = canvas.create_image(0,0,anchor =tkinter.NW,image = photo)
canvas.pack()
def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)

    time.sleep(1)
    frame = cv2.cvtColor(cv2.imread("sponsered.jpg"),cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)

    time.sleep(1.5)
    if decision =="notout":
        frame = cv2.cvtColor(cv2.imread("notout.jpg"),cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(cv2.imread("out.jpg"),cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)
stream = cv2.VideoCapture("clip.wmv")
def play(speed):
    print(f"you clicked on play . speed is {speed}")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    #frame = imutils.resize(frame,width = 650,height = 368)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)

def previous_fast(speed):
    pass
def previous_slow(speed):
    pass
def next_fast(speed):
   #print(f"u have given out with speed of {speed}")
   #canvas1= tkinter.Canvas(w,width=200,height=200)
   #image = PIL.Image.open("koala.jpg")
   #image = PIL.ImageTk.PhotoImage(image = image)
   #image_on_canvas_for_out= canvas1.create_image(0,0,anchor= tkinter.NW,image=image)
   #canvas1.pack()
   pass
def next_slow(speed):
    pass
def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("player is out")
def notout():
    thread = threading.Thread(target=pending,args=("notout",))
    thread.daemon=1
    thread.start()
btn1 = tkinter.Button(w,text = "<<Previous(fast)",width = 50,command=lambda:play(-25))
btn1.pack()
btn2 = tkinter.Button(w,text = "<<Previous(slow)",width = 50,command =lambda:play(-2))
btn2.pack()
btn3 = tkinter.Button(w,text = ">>Next(fast)",width = 50,command =lambda:play(25))
btn3.pack()
btn4 = tkinter.Button(w,text = ">>Next(slow)",width = 50,command =lambda:play(2))
btn4.pack()
btn5 = tkinter.Button(w,text ="Give_Out",width = 50,command=out)
btn5.pack()
btn6 = tkinter.Button(w,text = "Give_Not_Out",width = 50,command=notout)
btn6.pack()
w.mainloop()


####################

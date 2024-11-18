# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2023

@author: 5 Namune
"""

import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Crop Prediction System Using ML")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
# import required modules
  
  
# adjust window
root=tk.Tk()
root.geometry("200x200")
  
# loading the images
img = ImageTk.PhotoImage(Image.open("cor1.jpg")) 
img2= ImageTk.PhotoImage(Image.open("r1.jpg")) 
img3= ImageTk.PhotoImage(Image.open("crop2.jpg")) 
  
l=Label()
l.pack()
  
  
  
# using recursion to slide to next image
x = 1
  
# function to change to next image
def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    x = x+1
    root.after(2000, move)
  
# calling the function
move()
#
label_l1 = tk.Label(root, text="Agromarketing and Crop Prediction System Using ML",font=("Times New Roman", 30, 'bold'),
                    background="#152238", fg="white", width=50, height=1)
label_l1.place(x=200, y=20)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])

def agr():
    from subprocess import call
    call(["python","agromarketing.py"])
    
button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)

button2 = tk.Button(root, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=100, y=240)

button4 = tk.Button(root, text="Agromarketing",command=agr,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button4.place(x=100, y=380)

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def agr():
    from subprocess import call
    call(["python","agromarketing.py"])
def window():
  root.destroy()

button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=500, y=160)

button2 = tk.Button(root, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=500, y=240)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button3.place(x=500, y=330)

root.mainloop()
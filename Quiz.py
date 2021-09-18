from tkinter.constants import COMMAND
from tkinter.font import BOLD
from PIL import ImageTk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import Frame
from tkinter import RIDGE
from PIL import Image
import random
import time
from resizeimage import resizeimage

root = Tk()
root.title("Quiz")
root.geometry("1280x720+125+25")
root.resizable(False, False)

a=0
b=0
c=0
Label_1 = Label(root, text="                              Can You Win?", fg="white", bg="#053246", font=("times new roman", 45), width=182, height=2, anchor="w")
Label_1.pack()
Frame_1 = Frame(root, borderwidth=2, relief=RIDGE, bg="white")
Frame_1.place(x=125, y=215, width=681, height=325)
Label_2 = Label(root, text="     The Question", font=("times new roman", 20), width=45, height=1, fg="white", bg="#053246")
Label_2.place(x=125, y=205)
Label_3 = Label(root, text="     - You May or May not be able to Answer", anchor="w", fg="grey", bg="white", font=("Mv Boli", 10, "bold"), width=37, height=2)
Label_3.place(x=450, y=245)
Label_4 = Label(root, text="", fg="black", bg="white", font=("times new roman", 20, "bold"), width=40, height=1, borderwidth=3, relief="sunken")
Label_4.place(x=145, y=300)
Label_5 = Label(root, text="                              Time Left :", fg="black", bg="white", font=("times new roman", 20, "bold"), width=25, anchor="w", height=1)
Label_5.place(x=130, y=370)
Label_11 = Label(root, text="00:00", fg="black", bg="white", font=("times new roman", 20))
Label_11.place(x=485, y=370)
Label_12 = Label(root, text="Option 1", fg="black", bg="grey", font=("times new roman", 20))
Label_12.place(x=155, y=420, width=300)
Label_13 = Label(root, text="Option 2", fg="black", bg="grey", font=("times new roman", 20))
Label_13.place(x=475, y=420, width=300)
Label_14 = Label(root, text="Option 3", fg="black", bg="grey", font=("times new roman", 20))
Label_14.place(x=155, y=475, width=300)
Label_15 = Label(root, text="Option 4", fg="black", bg="grey", font=("times new roman", 20))
Label_15.place(x=475, y=475, width=300)
Frame_2 = Frame(root, borderwidth=4, bg="white")
Frame_2.place(x=900, y=205, width=322, height=330)
Label_18 = Label(root, text="Scores", font=("times new roman", 21), width=21, height=1, fg="white", bg="#053246")
Label_18.place(x=900, y=205)
Label_6 = Label(root, text="9B", fg="black", bg="white", font=("Times new roman", 30))
Label_6.place(x=935, y=270)
Label_7 = Label(root, text="9C", fg="black", bg="white", font=("Times new roman", 30))
Label_7.place(x=1115, y=270)
Label_8 = Label(root, text=a, fg="black", bg="white", font=("times new roman", 30))
Label_8.place(x=935, y=410)
Label_9 = Label(root, text=b, fg="black", bg="white", font=("times new roman", 30))
Label_9.place(x=1120, y=410)
Label_10 = Label(root, text="", fg="green", font=("times new roman", 30))
Label_10.place(x=940, y=550)

def correct():
    global a,b,c
    if c % 2 == 0:
        b = b+10
        Label_9.config(text=b)
    else:
        a = a+10
        Label_8.config(text=a)

def clear():
    Label_10.config(text="")
    Label_4.config(text="")
    Label_12.config(text="Option 1")
    Label_13.config(text="Option 2")
    Label_14.config(text="Option 3")
    Label_15.config(text="Option 4")
    Label_11.config(text="00:00")

def timer():
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:09")
    root.update()
    Label_11.config(text="00:09")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:08")
    root.update()
    Label_11.config(text="00:08")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:07")
    root.update()
    Label_11.config(text="00:07")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:06")
    root.update()
    Label_11.config(text="00:06")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:05")
    root.update()
    Label_11.config(text="00:05")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:04")
    root.update()
    Label_11.config(text="00:04")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:03")
    root.update()
    Label_11.config(text="00:03")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:02")
    root.update()
    Label_11.config(text="00:02")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:01")
    root.update()
    Label_11.config(text="00:01")
    root.update()
    time.sleep(1)
    root.update()
    Label_11.config(text="00:00")
    root.update()

def generate():
    global c
    c = c+1
    if c == 1:
        Label_4.config(text="Which of these is not a William Shakespeare creation?")
        Label_12.config(text="Much ado about nothing")
        Label_13.config(text="Hamlet")
        Label_14.config(text="Merchant of Venice")
        Label_15.config(text="Middlemarch")
        Label_11.config(text="00:10")
        root.after(1, timer)
    if c == 2:
        Label_4.config(text="Which of these is not a Charles Dickens creation?")
        Label_12.config(text="A Christmas carol")
        Label_13.config(text="David Copperfield")
        Label_14.config(text="The grapes of wrath")
        Label_15.config(text="Bleak house ")
        Label_11.config(text="00:10")
        root.after(1, timer)
    if c == 3:
        Label_4.config(text= "Which of these personalities invented fluoroscent lightning?", fg="black", bg="white", font=("times new roman", 19, "bold"), width=43, height=1, borderwidth=3, relief="sunken")
        Label_12.config(text="Nikola Tesla")
        Label_13.config(text="G.W. Carver")
        Label_14.config(text="Hedy Lamarr")
        Label_15.config(text="J. Gutenberg")
        Label_11.config(text="00:10")
        root.after(1, timer)
    if c == 4:
        Label_4.config(text="Which of these personalities invented printing press?", fg="black", bg="white", font=("times new roman", 20, "bold"), width=40, height=1, borderwidth=3, relief="sunken")
        Label_12.config(text="James Naismith")
        Label_13.config(text="J. Gutenberg")
        Label_14.config(text="Hedy Lamarr")
        Label_15.config(text="Benjamin Franklin")
        Label_11.config(text="00:10")
        root.after(1, timer)
    if c == 5:
        Label_4.config(text="What is the capital of Bulgaria?")
        Label_12.config(text="Sofia")
        Label_13.config(text="Minsk")
        Label_14.config(text="Bucharest")
        Label_15.config(text="Budapest")
        Label_11.config(text="00:10")
        root.after(1, timer)
    if c == 6:
        Label_4.config(text="What is the capital of Cyprus?")
        Label_12.config(text="Pristina")
        Label_13.config(text="Minsk")
        Label_14.config(text="Nicosia")
        Label_15.config(text="Prague")
        Label_11.config(text="00:10")
        root.after(1, timer)

Correct_button = Button(root, text="Correct", width=15,  borderwidth=5, bg="#00ff4c", fg="white", font=("times new roman", 20, BOLD), command=correct)
Correct_button.place(x=825, y=570, width=200)
InCorrect_button = Button(root, text="Incorrect", width=15,  borderwidth=5, bg="#ff2626", fg="white", font=("times new roman", 20, BOLD))
InCorrect_button.place(x=1050, y=570, width=200)
Submit_button = Button(root, text="QUESTION", width=25, height=1, borderwidth=5, bg="#053246", fg="white", font=("mv boli", 25), command=generate)
Submit_button.place(x=200, y=575, width=250, height=50)
Clear_button = Button(root, text="CLEAR", width=25, height=1, borderwidth=5, bg="#053246", fg="white", font=("mv boli", 25), command=clear)
Clear_button.place(x=500, y=575, width=250, height=50)

root.mainloop()
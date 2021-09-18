from PIL import ImageTk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import Frame
from tkinter import RIDGE
from PIL import Image
import qrcode
from tkinter import Toplevel
import resizeimage
import time
from resizeimage import resizeimage

root = Tk()
root.title("Qr Generator By Paramveer")
root.geometry("1280x720+125+25")
root.resizable(False, False)

Label_1 = Label(root, text="    QR Code Generator", fg="white", bg="#053246", font=("times new roman", 45), width=182, height=2, anchor="w")
Label_1.pack()
Frame_1 = Frame(root, borderwidth=2, relief=RIDGE, bg="white")
Frame_1.place(x=125, y=215, width=681, height=325)
Label_2 = Label(root, text="QR Details", font=("times new roman", 20), width=45, height=1, fg="white", bg="#053246")
Label_2.place(x=125, y=205)
Label_3 = Label(root, text="NAME  ", anchor="w", fg="black", bg="white", font=("times new roman", 20, "bold"), width=10, height=1)
Label_3.place(x=130, y=265)
Entry_1 = Entry(root, bg="white", fg="black", borderwidth=5, width=65)
Entry_1.place(x=350, y=267)
Label_4 = Label(root, text="CLASS  ", anchor="w", fg="black", bg="white", font=("times new roman", 20, "bold"), width=10, height=1)
Label_4.place(x=130, y=325)
Entry_2 = Entry(root, bg="white", fg="black", borderwidth=5, width=65)
Entry_2.place(x=350, y=327)
Label_5 = Label(root, text="ADMISSION NO.  ", fg="black", bg="white", font=("times new roman", 20, "bold"), width=25, anchor="w", height=1)
Label_5.place(x=130, y=383)
Entry_3 = Entry(root, bg="white", fg="black", borderwidth=5, width=65)
Entry_3.place(x=350, y=385)
Label_6 = Label(root, text="ROLL NO.", fg="black", bg="white", font=("times new roman", 20, "bold"), width=25, anchor="w", height=1)
Label_6.place(x=130, y=452)
Entry_4 = Entry(root, bg="white", fg="black", borderwidth=5, width=65)
Entry_4.place(x=350, y=454)
Frame_2 = Frame(root, borderwidth=2, bg="white")
Frame_2.place(x=900, y=205, width=322, height=330)
Label_2 = Label(root, text="QR Code", font=("times new roman", 21), width=21, height=1, fg="white", bg="#053246")
Label_2.place(x=900, y=205)
Label_7 = Label(Frame_2, text="No QR\nAvailable", font=("times new roman", 21), fg="black", bg="white")
Label_7.place(x=20, y=50, width=275, height=250)
Label_6 = Label(text="ALL FIELDS ARE REQUIRED", font=("times new roman", 40), fg="red")


def clear():
    Entry_1.delete(0, 'end')
    Entry_2.delete(0, 'end')
    Entry_3.delete(0, 'end')
    Entry_4.delete(0, 'end')
    Label_6.config(text="")
    Label_7.place(x=20, y=50)
    Label_7.config(image="")


def submit():

    value_1 = Entry_1.get()
    value_2 = Entry_2.get()
    value_3 = Entry_3.get()
    value_4 = Entry_4.get()

    if value_1 == "" or value_2 == "" or value_3 == "" or value_4 == "":
        Label_6.config(text="ALL FIELDS ARE REQUIRED", fg="red")
        Label_6.place(x=400, y=650, width=700, height=50)

    elif value_1 != "" and value_2 != "" and value_3 != "" and value_4 != "":
        global img
        value_1 = Entry_1.get()
        value_2 = Entry_2.get()
        value_3 = Entry_3.get()
        value_4 = Entry_4.get()
        Label_6.config(text="QR Generated Successfully", fg="green")
        Label_6.place(x=400, y=650, width=700, height=50)
        qr_data = f"Name:{value_1}\nClass:{value_2}\nAdmission No:{value_3}\nRoll No:{value_4}"
        qr = qrcode.make(qr_data)
        qr_1 = resizeimage.resize_cover(qr, [275, 250])
        qr_1.save("Qr for " + str(value_1) + ".png")
        img = ImageTk.PhotoImage(Image.open("Qr for " + str(value_1) + ".png"))
        Label_7.config(image=img)
    else:
        print('Some ERROR occured')


Submit_button = Button(root, text="GENERATE", width=25, height=1, borderwidth=5, bg="#053246", fg="white", font=("times new roman", 25), command=submit)
Submit_button.place(x=400, y=575, width=250, height=50)
Clear_button = Button(root, text="CLEAR", width=25, height=1, borderwidth=5, bg="#053246", fg="white", font=("times new roman", 25), command=clear)
Clear_button.place(x=700, y=575, width=250, height=50)

root.mainloop()

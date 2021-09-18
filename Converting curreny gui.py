import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Tk
from tkinter import Button
from forex_python import converter

root = Tk()
root.title("Hello world")
root.geometry("500x500")
root.resizable("False", "False")
root.config(bg="light grey")
c = converter.CurrencyRates()

def coverting_value():
    try:
        global c, entry_1
        a = entry_1.get()
        val = c.convert("USD", "INR", float(a))
        val = str(val)
        label_3 = Label(root, text=val , fg="black", bg="light grey", font=("comic sans ms", 35))
        label_3.place(x=0, y=400, width=500, height=50)
    except Exception as e:
        print(e)
        label_3 = Label(root, text="???????" , fg="red", bg="light grey", font=("times new roman", 35))
        label_3.place(x=0, y=400, width=500, height=50)

label_1 = Label(root, text="Currency Converter", fg="black", bg="light grey", font=("comic sans ms", 40))
label_1.place(x=0, y=0)
label_2 = Label(root, text="Amount in $", fg="black", bg="light grey", font=("comic sans ms", 35))
label_2.place(x=25, y=100)
entry_1 = Entry(root, fg="black", bg="light grey", font=("comic sans ms", 35))
entry_1.place(x=50, y=175, width=400, height=50)
button_1 = Button(root, text="CONVERT", fg="black", bg="light grey",command=coverting_value, font=("comic sans ms", 35))
button_1.place(x=150, y=245, height=75)
label_4 = Label(root, text="Amount in ₹", fg="black", bg="light grey", font=("comic sans ms", 35))
label_4.place(x=25, y=325)

root.mainloop()
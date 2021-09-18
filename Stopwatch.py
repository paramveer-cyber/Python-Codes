import tkinter
from tkinter import Label
from tkinter import Button
from tkinter import Tk

root = Tk()
root.title('Stopwatch')
root.geometry('300x250')
root.resizable(False, False)

seconds = 10
minute = 00
hour = 00
stop = 0


def start():
    global seconds, minute, hour
    global label_2
    seconds = seconds - 1
    if seconds == 0:
        stop = 1
    if seconds == 60:
        minute = 1
        seconds = 00
    if minute == 60:
        hour = 1
        minute = 00
    if stop == 0:
        val = f"{hour}:{minute}:{seconds}"
        label_2 = Label(root, text=val, font=('times new roman', 50))
        label_2.after(1000, start)
        label_2.place(x=5, y=80, relwidth=1, height=50)


def stop_1():
    global stop
    stop = 1


# noinspection PyGlobalUndefined
def reset():
    global stop, seconds, minute, hour, label_2
    seconds = 0
    hour = 0
    minute = 0
    if stop == 1:
        stop = 0


label_1 = Label(root, text="    Stopwatch", font=("times new roman", 25), bg='black', fg='white', anchor='w')
label_1.place(x=0, y=0, relwidth=1, height=50)
button_1 = Button(root, text="START", font=('times new roman', 20), fg='white', bg='black', command=start)
button_1.place(x=0, y=200, width=100, height=50)
button_2 = Button(root, text="STOP", font=('times new roman', 20), fg='white', bg='black', command=stop_1)
button_2.place(x=100, y=200, width=100, height=50)
button_3 = Button(root, text="RESET", font=('times new roman', 20), fg='white', bg='black', command=reset)
button_3.place(x=200, y=200, width=100, height=50)

root.mainloop()

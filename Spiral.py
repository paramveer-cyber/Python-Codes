from tkinter import *

# Defining Variables....
x0, y0, x1, y1 = 650, 350, 650, 350
gap, angle_1, angle_2 = 25, 1, 2

# Basic tkinter
root = Tk()
root.title("Spiral")
root.geometry("1280x720+125+25")
root.resizable(False, False)

# Canvas for Spiral
board = Canvas(root, bg = "black")
board.place(x = 0, y = 0, width=1280, height=720)

# Supporting Functions
def left():
    global x0, y0, x1, y1
    x1, y1 = x1-(gap*angle_2), y1
    board.create_line(x0, y0, x1, y1, fill="white", width=3)
    x0, y0 = x1, y1
    return x0, y0, x1, y1
def right():
    global x0, y0, x1, y1
    x1, y1 = x1+(gap*angle_1), y1
    board.create_line(x0, y0, x1, y1, fill="white", width=3)
    x0, y0 = x1, y1
    return x0, y0, x1, y1
def up():
    global x0, y0, x1, y1
    x1, y1 = x1, y1-(gap*angle_2)
    board.create_line(x0, y0, x1, y1, fill="white", width=3)
    x0, y0 = x1, y1
    return x0, y0, x1, y1
def down():
    global x0, y0, x1, y1
    x1, y1 = x1, y1+(gap*angle_1)
    board.create_line(x0, y0, x1, y1, fill="white", width=3)
    x0, y0 = x1, y1
    return x0, y0, x1, y1

# Main loop function 
def spiral(size):
    for i in range(size):
        global angle_1, angle_2
        right()
        down()
        left()
        up()
        angle_1, angle_2 = angle_1+2, angle_2+2

spiral(10)

root.mainloop()
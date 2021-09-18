import win32api
import time
import mouse

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)

state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128
while True:
    a = win32api.GetKeyState(0x01)
    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
            mouse.click('left')
        else:
            pass
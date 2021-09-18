import pyautogui
import time

time.sleep(5)
word = "NARUTO"

for i in range(1000):
    word = str(word)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(17)

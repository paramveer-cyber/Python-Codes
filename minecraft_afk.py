import random, time, pyautogui
list_1 = ["w", "a", "s", "d"]
time.sleep(3)
pyautogui.FAILSAFE = False
while True:
    key = random.choice(list_1)
    print(key)
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    time.sleep(2)

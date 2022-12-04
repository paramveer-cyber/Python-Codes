from pynput.mouse import Listener
import mouse, time

def on_click(x, y, button, pressed):
    mouse.click()

with Listener(on_click=on_click) as listener:
    listener.join()
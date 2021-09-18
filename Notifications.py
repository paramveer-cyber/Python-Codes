import win10toast
import time

while True:
    toaster = win10toast.ToastNotifier()
    toaster.show_toast('Drink water right now!!!', 'Drink water It''s been one hour!!!', duration=5)
    time.sleep(60 * 60)

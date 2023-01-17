import win10toast
import time

for i in range(4):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast('Eat Medicine!!!', 'Right now!!!', duration=5)
    time.sleep(60*10)

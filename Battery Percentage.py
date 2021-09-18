import psutil


def convert_Time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


battery = psutil.sensors_battery()
charging = battery.power_plugged

print("Battery percentage : ", battery.percent)
if charging:
    print("Plugged In")
else:
    print("Not Plugged In")

print("Battery Time left : ", convert_Time(battery.secsleft))

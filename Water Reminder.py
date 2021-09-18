from plyer import notification
import time

notification.notify(
            title="Please drink water Now!!!",
            message="It's been one hour, Drink the water right now!!!!",
            timeout=5
)
time.sleep(60*60)

import psutil
from plyer import notification
import time
battery = psutil.sensors_battery()
while(True):
    percent = battery.percent

    notification.notify(
        title="Battery percentage",
        message=str(percent) + "% battery remaining",
        timeout=10
    )
    time.sleep(60*60)

    continue
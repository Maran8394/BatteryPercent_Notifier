from psutil import sensors_battery
import time
from pynotifier import Notification
import sys



def run_code():
    increment = 0
    while not power_status:
        current_minute = time.localtime().tm_min

        if current_minute == increment:
            Notification(
                title="Battery Notification",
                description="{}% and {}min".format(percentage, current_minute),
                duration=5,
            ).send()
        else:
            time.sleep(6)
            
        increment = current_minute + 1


ar = sys.argv[1]
print(ar)

percentage = sensors_battery().percent
power_status = sensors_battery().power_plugged  
if ar == 'start':
    run_code()

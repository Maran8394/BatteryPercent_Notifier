from psutil import sensors_battery
import time
from pynotifier import Notification
import sys



def run_code(percentage, power_status):
    next_ten_min = 0
    print(next_ten_min)
    while power_status:
        current_minute = time.localtime().tm_min

        if current_minute == next_ten_min:
            Notification(
                title="Battery Notification",
                description="{}% and {}min".format(percentage, current_minute),
                duration=5,
            ).send()
        else:
            time.sleep(120) # for 10min sleep
        print("current_minute", current_minute)    
        next_ten_min = current_minute + 2
        print("next_ten_min",next_ten_min)



percentage = sensors_battery().percent # to get percentage of the battery
power_status = sensors_battery().power_plugged  # to get the power status which is plugged or unplugged

start_arg = sys.argv[1]
if start_arg == 'start':
    run_code(percentage, power_status)
else:
    print("Enter valid argument")

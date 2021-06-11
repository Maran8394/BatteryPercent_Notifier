from psutil import sensors_battery # for Battery details
import time
from pynotifier import Notification # for notification
import sys



def run_code(percentage, power_status):
    try:
        next_ten_min = 0
        print("SCRIPT STARTED")
        
        # print(next_ten_min)
        while power_status:
            current_minute = time.localtime().tm_min

            if current_minute == next_ten_min:
                Notification(
                    title="Battery Notification",
                    description="{}% and {}min".format(percentage, current_minute),
                    duration=5,
                ).send()    

            else:
                
                print("current_minute", current_minute)    
                next_ten_min = current_minute + 1
                print("next_ten_min",next_ten_min)
                time.sleep(59)

        else:
            Notification(
                    title="Battery on Charging",
                    description="This script is developed for only on off-charging ",
                    duration=5,
                ).send()
            print("ENDED")


    except KeyboardInterrupt as e:
        print("You're stop the script.....")

    except:
        print("Some malfunction occured.....")



percentage = sensors_battery().percent # to get percentage of the battery
power_status = sensors_battery().power_plugged  # to get the power status which is plugged or unplugged

start_arg = sys.argv[1]
if start_arg == 'start':
    run_code(percentage, power_status)
else:
    print("Enter valid argument")

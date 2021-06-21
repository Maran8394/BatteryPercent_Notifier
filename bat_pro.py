from psutil import sensors_battery
from sys import exit, argv
from time import sleep
from pynotifier import Notification
from time import localtime as l

def notification(string):
    Notification(
        title="Battery Percentage Notifier",
        description=string,
        duration=5,
        ).send()


def starter():
    try:
        power_status = sensors_battery().power_plugged
        while not power_status:
            b_percent = sensors_battery().percent
            notification(string="{}% left".format(b_percent))
            min_now = l().tm_min
            sec_now = l().tm_sec
            print("{percent}% Left {mint}min {sec}sec".format(percent=b_percent, mint=min_now, sec=sec_now))
            sleep(600) 
            
        else:
            print("System on Charging....")
            notification(string="System on Charging")
            exit()

    except KeyboardInterrupt:
        print("KeyBoardInterrupt Error Encounterd")

if __name__ == '__main__':
    if argv[1] == 'start':
        starter()

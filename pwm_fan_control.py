#!/usr/bin/python3

import RPi.GPIO as IO
import time
import subprocess

servo = 13
IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(servo,IO.OUT)
fan = IO.PWM(servo,200)
fan.start(0)

while 1:
    #get CPU temp
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000.00
    temp = float('%.2f' % temp)
    file.close()
    # temp = get_temp()                      # Get the current CPU temperature
    if temp > 70:                            # Check temperature threshhold, in degrees celcius
        fan.ChangeDutyCycle(100)             # Set fan duty based on temperature, 100 is max speed and 0 is min speed or off.
    elif temp > 60:
        fan.ChangeDutyCycle(85)
    elif temp > 50:
        fan.ChangeDutyCycle(60)
    elif temp > 40:
        fan.ChangeDutyCycle(50)
    elif temp > 32:
        fan.ChangeDutyCycle(45)
    elif temp > 25:
        fan.ChangeDutyCycle(40)
    else:
        fan.ChangeDutyCycle(0)
    time.sleep(5)                            # Sleep for 5 seconds

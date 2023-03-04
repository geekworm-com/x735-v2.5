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

def get_temp():
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not get temperature')
while 1:
    temp = get_temp()                        # Get the current CPU temperature
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

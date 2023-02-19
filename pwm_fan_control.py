#!/usr/bin/python3

import RPi.GPIO as IO
import time
import subprocess

# constants
SERVO_PIN = 13
FAN_FREQ = 25000                             # Use a constant for the fan PWM frequency
TEMP_THRESHOLD = [70, 60, 50, 40, 32, 25, -100]  # Use a list to store temperature thresholds
DUTY_CYCLE = [100, 85, 70, 50, 25, 15, 0]  # Use a list to store corresponding duty cycles

IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(SERVO_PIN, IO.OUT)
fan = IO.PWM(SERVO_PIN, FAN_FREQ)
fan.start(0)

def get_temp():
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode().strip()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not get temperature')

while True:  # Use True instead of 1 for clarity
    temp = get_temp()
    for i, threshold in enumerate(TEMP_THRESHOLD):
        if temp > threshold:
            fan.ChangeDutyCycle(DUTY_CYCLE[i])
            break  # Stop checking once the first threshold is exceeded
    time.sleep(5)

#!/usr/bin/python
# this python code is base python 3, not python 2
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import logging

TACH = 16
PULSE = 2
WAIT_TIME = 1

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TACH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

t = time.time()
rpm = 0

def fell(n):
    global t
    global rpm

    dt = time.time() - t
    if dt < 0.005: return

    freq = 1 / dt
    rpm = (freq / PULSE) * 60
    t = time.time()

GPIO.add_event_detect(TACH, GPIO.FALLING, fell)

try:
    while True:
        # print "%.f RPM" % rpm
        print("%.f RPM" % rpm)
        rpm = 0
        time.sleep(WAIT_TIME)

except KeyboardInterrupt:
    logging.info('Exiting...')
finally:
    # Clean up the GPIO resources
    GPIO.cleanup()

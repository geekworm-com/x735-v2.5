#!/usr/bin/python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import logging

TACH = 16
PULSE = 2
WAIT_TIME = 1

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

class RPMCounter:
    def __init__(self, pin):
        self.pin = pin
        self.rpm = 0
        self.last_time = time.time()

        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.FALLING, self._update_rpm)

    def _update_rpm(self, channel):
        dt = time.time() - self.last_time
        if dt < 0.005:
            return

        freq = 1 / dt
        self.rpm = (freq / PULSE) * 60
        self.last_time = time.time()

    def get_rpm(self):
        current_rpm = self.rpm
        self.rpm = 0
        return current_rpm

if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        rpm_counter = RPMCounter(TACH)

        while True:
            rpm = rpm_counter.get_rpm()
            logging.info('Current RPM: {:.2f}'.format(rpm))
            time.sleep(WAIT_TIME)

    except KeyboardInterrupt:
        logging.info('Exiting...')
    finally:
        # Clean up the GPIO resources
        GPIO.cleanup()

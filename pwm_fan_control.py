#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

# configuration
fan_pin = 13
temp_pwm_curve = [ (30,30), (50,50), (55,75), (60,90), (80,100) ]
fan_threshold_temp = 30

# initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fan_pin, GPIO.OUT)
pwm = GPIO.PWM(fan_pin, 25000)
pwm.start(0)

# control loop
try:
     while(1):
          #get CPU temp
          file = open("/sys/class/thermal/thermal_zone0/temp")
          temp = float(file.read()) / 1000.00
          temp = float('%.2f' % temp)
          file.close()

          if(temp < fan_threshold_temp):
               pwm.ChangeDutyCycle(0)
          else:
               for item in temp_pwm_curve:
                    if(temp > item[0]):
                         pwm.ChangeDutyCycle(item[1])

          time.sleep(1)

except:
    pwm.stop()
    GPIO.cleanup()

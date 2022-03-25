#!/usr/bin/python
import RPi.GPIO as GPIO
import time

try:
     GPIO.setmode(GPIO.BCM)
     GPIO.setwarnings(False)
     GPIO.setup(13, GPIO.OUT)
     pwm = GPIO.PWM(13, 25000)

     while(1):
          #get CPU temp
          file = open("/sys/class/thermal/thermal_zone0/temp")
          temp = float(file.read()) / 1000.00
          temp = float('%.2f' % temp)
          file.close()

          if(temp > 30):
               pwm.start(40)

          if(temp > 50):
               pwm.start(50)

          if(temp > 55):
               pwm.start(75)

          if(temp > 60):
               pwm.start(90)

          if(temp > 65):
               pwm.start(100)

          if(temp < 30):
               pwm.start(0)
          time.sleep(2)


except KeyboardInterrupt:
    GPIO.cleanup()


#!/usr/bin/python
import pigpio
import time

servo = 13

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo, 25000 )
pwm.set_PWM_range(servo, 100)
while(1):
     #get CPU temp
     file = open("/sys/class/thermal/thermal_zone0/temp")
     temp = float(file.read()) / 1000.00
     temp = float('%.2f' % temp)
     file.close()

     if(temp > 30):
          pwm.set_PWM_dutycycle(servo, 40)

     if(temp > 50):
          pwm.set_PWM_dutycycle(servo, 50)

     if(temp > 55):
          pwm.set_PWM_dutycycle(servo, 75)

     if(temp > 60):
          pwm.set_PWM_dutycycle(servo, 90)

     if(temp > 65):
          pwm.set_PWM_dutycycle(servo, 100)

     if(temp < 30):
          pwm.set_PWM_dutycycle(servo, 0)
     time.sleep(1)

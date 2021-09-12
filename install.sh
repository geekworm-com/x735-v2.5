#IMPORTANT! This script is only for the X735 V2.5
#x725 V2.5 Powering on /reboot /full shutdown through hardware
#!/bin/bash

#sudo sed -e '/shutdown/ s/^#*/#/' -i /etc/rc.local

echo '#!/bin/bash

SHUTDOWN=5
REBOOTPULSEMINIMUM=200
REBOOTPULSEMAXIMUM=600
echo "$SHUTDOWN" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio$SHUTDOWN/direction
BOOT=12
echo "$BOOT" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$BOOT/direction
echo "1" > /sys/class/gpio/gpio$BOOT/value

echo "X735 Shutting down..."

while [ 1 ]; do
  shutdownSignal=$(cat /sys/class/gpio/gpio$SHUTDOWN/value)
  if [ $shutdownSignal = 0 ]; then
    /bin/sleep 0.2
  else
    pulseStart=$(date +%s%N | cut -b1-13)
    while [ $shutdownSignal = 1 ]; do
      /bin/sleep 0.02
      if [ $(($(date +%s%N | cut -b1-13)-$pulseStart)) -gt $REBOOTPULSEMAXIMUM ]; then
        echo "X735 Shutting down", SHUTDOWN, ", halting Rpi ..."
        sudo poweroff
        exit
      fi
      shutdownSignal=$(cat /sys/class/gpio/gpio$SHUTDOWN/value)
    done
    if [ $(($(date +%s%N | cut -b1-13)-$pulseStart)) -gt $REBOOTPULSEMINIMUM ]; then
      echo "X735 Rebooting", SHUTDOWN, ", recycling Rpi ..."
      sudo reboot
      exit
    fi
  fi
done' > /etc/x735pwr.sh
sudo chmod +x /etc/x735pwr.sh
sudo sed -i '$ i /etc/x735pwr.sh &' /etc/rc.local

#X735 full shutdown through Software
#!/bin/bash

#sudo sed -e '/button/ s/^#*/#/' -i /etc/rc.local

echo '#!/bin/bash

BUTTON=20

echo "$BUTTON" > /sys/class/gpio/export;
echo "out" > /sys/class/gpio/gpio$BUTTON/direction
echo "1" > /sys/class/gpio/gpio$BUTTON/value

SLEEP=${1:-4}

re='^[0-9\.]+$'
if ! [[ $SLEEP =~ $re ]] ; then
   echo "error: sleep time not a number" >&2; exit 1
fi

echo "X735 Shutting down..."
/bin/sleep $SLEEP

echo "0" > /sys/class/gpio/gpio$BUTTON/value
' > /usr/local/bin/x735softsd.sh
sudo chmod +x /usr/local/bin/x735softsd.sh
sudo systemctl enable pigpiod

USER_RUN_FILE=/home/pi/.bashrc
CUR_DIR=$(pwd)
sudo echo "alias x735off='sudo x735softsd.sh'" >> ${USER_RUN_FILE}
sudo echo "python3 ${CUR_DIR}/pwm_fan_control.py&"  >> ${USER_RUN_FILE}

sudo pigpiod
python3 ${CUR_DIR}/pwm_fan_control.py &

echo "The installation is complete."
echo "Please run 'sudo reboot' to reboot the device."
echo "NOTE:"
echo "1. DON'T modify the name fold: $(basename ${CUR_DIR}), or the PWM fan will not work after reboot."
echo "2. pwm_fan_control.py is python file to control fan speed according temperature of CPU, you can modify it according your needs."
echo "3. PWM fan needs a PWM signal to start working. If fan doesn't work in third-party OS afer reboot only remove the YELLOW and BLUE wire of x735 fan to let the fan run immediately or contact us: info@geekworm.com."

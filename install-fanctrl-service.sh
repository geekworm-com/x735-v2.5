#!/bin/bash
# Copies the python script to /opt/x735/pwm_fan_control.py,
# configures a systemd unit `fanctrl.service`, enables and starts it.
#
# If you change $x735Dir, make sure you update it in the `fanctrl.service` file too.
if [ "$EUID" != "0" ];
then
    echo -e "\033[31m This script must be run as root\033[0m"
    exit 1;
fi

x735Dir=/opt/x735
mkdir -p "$x735Dir"

cp pwm_fan_control.py "${x735Dir}/pwm_fan_control.py"
chown -R root:root "${x735Dir}"
chmod 0644 "${x735Dir}/pwm_fan_control.py"

cp fanctrl.service /etc/systemd/system/fanctrl.service
systemctl daemon-reload
systemctl enable fanctrl.service
systemctl start fanctrl.service

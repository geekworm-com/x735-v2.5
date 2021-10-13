#!/bin/bash

# Author: Tranko (https://github.com/thorkseng/x
# Create a small service that start when the pi stars.
# This avoid to have it in bashrc and wait until the user logon.
# This avoid the issue that if you logon several times ir runned several times.

# Create the service
echo "Creating the service in /etc/systemd/system/ with name x735fan.service"
sudo cat > /etc/systemd/system/x735fan.service <<EOF
[Unit]
Description=x735 Fan Service
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 $HOME/x735-v2.5/pwm_fan_control.py

[Install]
WantedBy=multi-user.target
EOF

# Reload the daemon
echo "Reload the systemd daemon"
sudo systemctl daemon-reload

# Enable the service to be enabled on startup
echo "Enable the new service (it will start in any reboot of the system)."
sudo systemctl enable x735fan.service

# Start the service
echo "Start the service"
sudo systemctl start x735fan.service

# Check that the service is running fine
# sudo systemctl status x735fan.service | grep "started"
STATUS="$(systemctl is-active x735fan.service)"
if [ "${STATUS}" = "active" ]; then
    echo "Service is active and running correctly"
else
    echo "Service not running something was wrong."
    exit 1
fi

# If everything goes fine, remove the included py script in .bashrc
# Delete local .bashrc lines that are not longer needed to start the fan
echo "Detelete the execution of pwm_fan_control from the file .bashrc"
sed -i '/pwm_fan_control.py/d' $HOME/.bashrc

# Additional notes
echo "Everything going fine"
echo "Now the fan will start in any reboot of the system\n"
echo "You can control the service with the next commands:"
echo "Check the status of the service: sudo systemctl status x735fan.service"
echo "Stop the service: sudo systemctl stop x735fan.service"
echo "Restart the service: sudo systemctl restart x735fan.service"
echo "Check the logs of the service: journalctl -u x735fan.service"
echo "Edit the service configuration in: /etc/systemd/system/x735fan.service"


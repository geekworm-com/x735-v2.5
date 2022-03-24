# Create pigpiod service - begin
#!/bin/bash

SERVICE_NAME="/lib/systemd/system/pigpiod.service"
# Create service file on system.
if [ -e $SERVICE_NAME ]; then
	sudo rm $SERVICE_NAME -f
fi

sudo echo '[Unit]
Description=Daemon required to control GPIO pins via pigpio
[Service]
ExecStart=/usr/local/bin/pigpiod
ExecStop=/bin/systemctl kill pigpiod
Type=forking
[Install]
WantedBy=multi-user.target
' >> ${SERVICE_NAME}

# create pigpiog service - begin

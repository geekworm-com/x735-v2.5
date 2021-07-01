#!/bin/bash
#remove x-c1 old installtion
sudo sed -i '/x735/d' ~/.bashrc
sudo sed -i '/x735/d' /etc/rc.local

sudo rm /usr/local/bin/x735softsd.sh -f
sudo rm /etc/x735pwr.sh -f

sudo systemctl disable pigpiod

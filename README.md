# x735-v2.5
This is the safe shutdown script and some python sample code.

from: https://wiki.geekworm.com/X735_V2.5_Software
> install
Assuming your system is updated, add these packages:
```
sudo apt-get install python-smbus
sudo apt-get install pigpio python-pigpio python3-pigpio
```

Copy the scripts from github (needs to be updated to s/geekworm-com/jg3/ in case their files disappear)
```
git clone https://github.com/geekworm-com/x735-v2.5
```

Now that you have those files get into that directory, make the script executable, and run it.  This creates a /usr/local/bin/x735softsd.sh script for the button press:
```
cd x735-v2.5
sudo chmod +x *.sh
sudo bash install.sh
sudo reboot
```

>uninstall
```
sudo ./uninstall.sh
```
>read-fan-speed.py
```
sudo ./read_fan_speed.py
```
After a reboot, we can run ```sudo read_fan_speed.py``` to get an update on the fan's current speed.  Nice!

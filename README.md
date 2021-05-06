# x735-v2.5
This is the safe shutdown script and some python sample code.

from: https://wiki.geekworm.com/X735_V2.5_Software



Assuming your system is updated, add these packages:
```
sudo apt-get install python-smbus 
sudo apt-get install pigpio python-pigpio python3-pigpio
```

Copy the scripts from github (needs to be updated to s/geekworm-com/jg3/ in case their files disappear)
```
git clone https://github.com/geekworm-com/x735-v2.5.git
```

Now that you have those files get into that directory, make the script executable, and run it.  This creates a /usr/local/bin/x735softsd.sh script for the button press:
```
cd x735-v2.5
sudo chmod +x x735-v25.sh
sudo bash x735-v25.sh
```


Now, those python scripts.

Let's put these in a place where we know where they are assuming you're still in the directory where you pulled the files from github down ...
```
chmod u+x *.py
sudo cp *.py /usr/local/bin/.
```

Now we need to add ```@reboot python3 /usr/local/bin/pwm_fan_control.py``` to the end of crontab, but you can't just ```>>>``` crontab so  use ```crontab -e``` to add that line to the bottom of the file.

After a reboot, we can run ```sudo read_fan_speed.py``` to get an update on the fan's current speed.  Nice!


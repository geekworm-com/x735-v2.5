# x735-v2.5 for Python3 + Debian Bullseye / Debian 11

## Installation
This scripts are tested on RaspiaOS 64 bits upgraded to Debian Bullseye.
You should use the next guide (based on the [official website of the GeekWorm X735](https://wiki.geekworm.com/X735_V2.5_Software).
This packages are upgrade to use Python3 (Python2 is deprecated):

    sudo apt install python3 python3-smbus python3-pigpio
    sudo apt install pigpio
    sudo apt install git
    git clone https://github.com/thorkseng/x735-v2.5/
    cd x735-v2.5
    sudo chmod +x *.sh
    sudo bash install.sh
    sudo reboot

## Usage
For activate the fan manually you can do with the next command, also, this command is added (in background) in the .bashrc of the profile of the user:

    python3 pwm_fan_control.py

For read the speed of the system you need to use python3 instead python

    python3 read_fan_speed.py 

## Credits
Based on the [GeekWorm user guide](https://wiki.geekworm.com/X735_V2.5_Software) and the original [repository of GeekWorm.com](https://github.com/geekworm-com/x735-v2.5)

Feel free to copy and modify :)

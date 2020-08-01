#!/bin/sh
#launcher.sh
# Navigate and execute the main.py script then navigate back to root folder

cd /
cd home/pi/iot/piot1

rm -R cronlog
sudo python auto.py

cd /
cd home/pi


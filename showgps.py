#!/usr/bin/env python

from OmegaExpansion import oledExp
import time
import json
import os

oledExp.setVerbosity(0)
oledExp.setTextColumns()
oledExp.driverInit()

oledExp.drawFromFile("/smb/scripts/dragon.lcd")
time.sleep(5)

oledExp.driverInit()
oledExp.setCursor(0, 0)
oledExp.write("+-------------------+")
oledExp.setCursor(1, 0)
oledExp.write("| Current GPS Info: |")
oledExp.setCursor(2, 0)
oledExp.write("+---------+---------+")

if os.path.getsize('/smb/scripts/gpsinfo.txt') == 0:
	oledExp.setCursor(4, 0)
	oledExp.write("GPS Info doesnt seem")
	oledExp.setCursor(5, 0)
	oledExp.write("to exist.")
	oledExp.setCursor(6, 0)
	oledExp.write("Check GPSInfo file.")
	exit()

with file('/smb/scripts/gpsinfo.txt', 'r') as gpsfile:
	gpsinfo = json.load(gpsfile)

time.sleep(2)

if gpsinfo.has_key('signal'):
	oledExp.setCursor(4, 0)
	oledExp.write("No GPS signal found")
	oledExp.setCursor(5, 0)
	oledExp.write("Please try later!")
elif gpsinfo.has_key('latitude'):
	oledExp.setCursor(3, 0)
	oledExp.write("Latitude  | "+gpsinfo['latitude'])
	oledExp.setCursor(4, 0)
	oledExp.write("Longitude | "+gpsinfo['longitude'])
	oledExp.setCursor(5, 0)
	oledExp.write("Elevation | "+gpsinfo['elevation'])
	oledExp.setCursor(6, 0)
	oledExp.write("Course    | "+gpsinfo['course'])
	oledExp.setCursor(7, 0)
	oledExp.write("Speed     | "+gpsinfo['speed'])

exit()

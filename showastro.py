#!/usr/bin/env python

# Set up the different libraries used in the script.
from OmegaExpansion import oledExp
import urllib2
import json
import os

# Initialize and clear the OLED screen.
oledExp.setVerbosity(0)
oledExp.setTextColumns()
oledExp.driverInit()

# Read the information gathered from the GPS expansion
# Make sure to change the directory to match where this file lives.
with file('/smb/scripts/gpsastro.txt', 'r') as gpsfile:
	gpsinfo = json.load(gpsfile)

# Check to see that the GPS expansion actually pulled the location
if gpsinfo.has_key('signal'):
	oledExp.setCursor(3, 0)
	oledExp.write("No GPS signal found")
	oledExp.setCursor(5, 0)
	oledExp.write("Please try later!")
	exit()

# Pull the data from Weather Underground based on location and using your own API key.
# Get your own API key from https://www.wunderground.com/weather/api
APIKey = '<your api key>'
astrodata = urllib2.urlopen("http://api.wunderground.com/api/"+APIKey+"/astronomy/q/"+gpsinfo['latitude']+","+gpsinfo['longitude']+".json")
astroinfo = json.loads(astrodata.read())

# Write data out to the OLED screen and then Exit.
oledExp.setCursor(0, 0)
oledExp.write("Sun and Moon Info")
oledExp.setCursor(1, 0)
oledExp.write("=====================")
oledExp.setCursor(2, 0)
oledExp.write("Sunrise    : "+astroinfo['moon_phase']['sunrise']['hour']+":"+astroinfo['moon_phase']['sunrise']['minute'])
oledExp.setCursor(3, 0)
oledExp.write("Sunset     : "+astroinfo['moon_phase']['sunset']['hour']+":"+astroinfo['moon_phase']['sunset']['minute'])
oledExp.setCursor(4, 0)
oledExp.write("Moonlight  : "+astroinfo['moon_phase']['percentIlluminated']+" %")
oledExp.setCursor(5, 0)
oledExp.write("Hemisphere : "+astroinfo['moon_phase']['hemisphere'])
oledExp.setCursor(6, 0)
oledExp.write("Phase : "+astroinfo['moon_phase']['phaseofMoon'])

exit()

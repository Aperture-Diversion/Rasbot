#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
import os
from twython import Twython

# API STUFF
CONSUMER_KEY = '*'
CONSUMER_SECRET = '*'
ACCESS_KEY = '*'
ACCESS_SECRET = '*'
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# RANDOMLY POSTS CPU TEMPERATURE, WHY WOULD ANYONE WANT TO KNOW THIS?
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

if float(temp) >= 45:
  extra = 'pretty hot ;)'
elif float(temp) <= 30:
  extra = 'really cool 8)'
else:
  extra = 'ok :/'

twitter.update_status(status='In case you want to know, my current CPU temperature is about ' + temp + ' °C. I am ' + extra  + ' #IoT #RaspberryPi')

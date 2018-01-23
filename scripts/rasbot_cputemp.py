#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
from os import popen
from twython import Twython
from rasbot_twython import auth

# API STUFF
twitter = auth()

# RANDOMLY POSTS CPU TEMPERATURE, WHY WOULD ANYONE WANT TO KNOW THIS?
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

if float(temp) >= 45.0:
  extra = 'pretty hot ;)'
elif float(temp) <= 30.0:
  extra = 'really cool 8)'
elif float(temp) <= 40.0:
  extra = 'fine ._.'
else:
  extra = 'ok :/'

twitter.update_status(status='In case you want to know, my current CPU temperature is about ' + str(temp) + ' °C. I am ' + extra  + ' #IoT #RaspberryPi')

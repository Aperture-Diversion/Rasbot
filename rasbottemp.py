#!/usr/bin/env python
#   version: 1.2

import sys
import os
from twython import Twython

CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

rasbot = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# Automatically reads the CPU temperature and posts it together with the little text below.
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
rasbot.update_status(status='My current CPU temperature is about '+temp+' C . I am really cool! :P #IoT #RaspberryPi')
#!/usr/bin/env python
import sys
import os

from twython import Twython
CONSUMER_KEY = '--SECRET--'
CONSUMER_SECRET = '--SECRET--'
ACCESS_KEY = '--SECRET--'
ACCESS_SECRET = '--SECRET--'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
api.update_status(status='My current CPU temperature is about '+temp+' C . I am quite hot, am I? :P #IoT #RaspberryPi')

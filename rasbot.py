#!/usr/bin/env python
#   version: 1.2

import sys
from twython import Twython

CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

rasbot = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# Command: sudo python /path/to/your/file/rasbot.py 'your message comes here'
rasbot.update_status(status=sys.argv[1])
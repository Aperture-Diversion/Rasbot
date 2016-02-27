#!/usr/bin/env python
import sys
from twython import Twython

CONSUMER_KEY = '--SECRET--'
CONSUMER_SECRET = '--SECRET--'
ACCESS_KEY = '--SECRET--'
ACCESS_SECRET = '--SECRET--'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])

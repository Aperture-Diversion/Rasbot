#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
import sys
from twython import Twython

# API STUFF
CONSUMER_KEY = '*'
CONSUMER_SECRET = '*'
ACCESS_KEY = '*'
ACCESS_SECRET = '*'
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# CREATE A SIMPLE TWEET
twitter.update_status(status=sys.argv[1])

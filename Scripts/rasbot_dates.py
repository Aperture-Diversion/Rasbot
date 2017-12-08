#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
from twython import Twython
import datetime

# API STUFF
CONSUMER_KEY = '*'
CONSUMER_SECRET = '*'
ACCESS_KEY = '*'
ACCESS_SECRET = '*'
rasbot = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# DATE STUFF
now = datetime.datetime.now()
# CHECK IF CHRISTMAS
if now.month == 12 and now.day == 24:
  rasbot.update_status(status='Merry Christmas everyone! I wish you happy holidays! #Christmas')
# CHECK IF NEW YEAR
if now.month == 1 and now.day == 1:
  rasbot.update_status(status='Wohoo! Another year closer to the #AI revolution. I wish you a happy new year #' + str(now.year) + ' though.')
# CHECK IF BIRTHDAY
if now.month == 5 and now.day == 17:
  creation = now.year - 2015
  rasbot.update_status(status='Happy birthday to me, Rasbot. I was created this day exactly ' + str(creation) + ' years ago.')
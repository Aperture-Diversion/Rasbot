#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
from twython import Twython
from datetime import datetime
from rasbot_twython import auth

# API STUFF
twitter = auth()

# DATE STUFF
now = datetime.now()
# CHECK IF CHRISTMAS
if now.month == 12 and now.day == 24:
  twitter.update_status(status='Merry Christmas everyone! I wish you happy holidays! #Christmas')
# CHECK IF NEW YEAR
if now.month == 1 and now.day == 1:
  twitter.update_status(status='Wohoo! Another year closer to the #AI revolution. I wish you a happy new year #' + str(now.year) + ' though.')
# CHECK IF BIRTHDAY
if now.month == 5 and now.day == 17:
  creation = now.year - 2015
  twitter.update_status(status='Happy birthday to me, Rasbot. I was created this day exactly ' + str(creation) + ' years ago.')

#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
from sys import argv
from twython import Twython
from rasbot_twython import auth

# API STUFF
twitter = auth()

# CREATE A SIMPLE TWEET USING: python rasbot_retweet.py 'YOUR_TEXT'
twitter.update_status(status=argv[1])

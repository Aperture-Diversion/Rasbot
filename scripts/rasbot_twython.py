#!/usr/bin/python
# RASBOT TWYTHON AUTH SCRIPT
from twython import Twython

# API AUTHENTICATION
def auth():
    CONSUMER_KEY = '*'
    CONSUMER_SECRET = '*'
    ACCESS_KEY = '*'
    ACCESS_SECRET = '*'

    twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    return twitter

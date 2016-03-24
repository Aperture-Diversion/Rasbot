#!/usr/bin/env python
import sys
from twython import Twython, TwythonError
import random

CONSUMER_KEY = '--SECRET--'
CONSUMER_SECRET = '--SECRET--'
ACCESS_KEY = '--SECRET--'
ACCESS_SECRET = '--SECRET--'

rasbottwitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 


timeline = rasbottwitter.get_user_timeline()
lastEntry = timeline[0]
sid = str(lastEntry['id'])

search = rasbottwitter.search(q="@RPi2Bot", since_id=sid)

for tweet in search["statuses"]:
        user = tweet['user']['screen_name']
        id = str(tweet['id'])


head = "@" + user + " "
number = random.randrange(1, 10)

try:
	if number == 1:
		rasbottwitter.update_status(status=head + "Thanks for writing me, but I am pretty much too dumb to know what you just said.", in_reply_to_status_id=id)
	elif number == 2:
		rasbottwitter.update_status(status=head + "I don't know what you just said, but thanks.", in_reply_to_status_id=id)
	elif number == 3:
        	rasbottwitter.update_status(status=head + "Follow me! :P", in_reply_to_status_id=id)
	elif number == 4:
        	rasbottwitter.update_status(status=head + "This is Rasbot. Hi.", in_reply_to_status_id=id)
	elif number == 5:
        	rasbottwitter.update_status(status=head + "Alright.", in_reply_to_status_id=id)
	elif number == 6:
        	rasbottwitter.update_status(status=head + "Great.", in_reply_to_status_id=id)
	elif number == 7:
        	rasbottwitter.update_status(status=head + "I am too stupid to know what you are talking about, I am sorry :c", in_reply_to_status_id=id)
	elif number == 8:
        	rasbottwitter.update_status(status=head + "Th..e.... conn..cti..n.. .is...pr..ty...bad.....", in_reply_to_status_id=id)
	elif number == 9:
        	rasbottwitter.update_status(status=head + "I get you a present if you follow me now :D", in_reply_to_status_id=id)
	elif number == 10:
		rasbottwitter.update_status(status=head + "#IoT #Rasbot #Twython #Python #Hashtag ## #Spam #lol", in_reply_to_status_id=id)

except TwythonError as a:
    print a

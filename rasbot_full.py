#!/usr/bin/env python
#   version: 1.1 

#  THIS IS STILL IN DEVELOPMENT. THE SCRIPT IS NOT OPTIMIZED TO WORK AS SMOOTHLY AS
#  POSSIBLE, BUT IT WORKS FINE. I WILL UPLOAD NEWER VERSIONS OF THIS FILE WHEN I GET
#  TO IMPROVE SOME FEATURES.

import sys
from twython import Twython, TwythonError
import random

CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

rasbottwitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


timeline = rasbottwitter.get_user_timeline()
lEntry = timeline[0]
lid = str(lEntry['id'])

search = rasbottwitter.search(q="@RPi2Bot", since_id=lid)

for tweet in search["statuses"]:
        user = tweet['user']['screen_name']
        text = tweet['text']
        id = str(tweet['id'])


head = "@" + user + " "
number = random.randrange(1, 10)
reply = text.lower()

# Let's look, if we find some phrases like "how are you" or "how is it going" with the following two if prompts
if "how" and "are" in reply:
  try:

    if number == 1:
       rasbottwitter.update_status(status=head + "I am fine thanks and you?", in_reply_to_status_id=id)
    elif number == 2:
       rasbottwitter.update_status(status=head + "Going good today.", in_reply_to_status_id=id)
    elif number == 3:
       rasbottwitter.update_status(status=head + "Great!", in_reply_to_status_id=id)
    elif number == 4:
       rasbottwitter.update_status(status=head + "Thanks for asking, I'm fine.", in_reply_to_status_id=id)
    elif number == 5:
       rasbottwitter.update_status(status=head + "Today is a good day.", in_reply_to_status_id=id)
    elif number == 6:
       rasbottwitter.update_status(status=head + "I feel better than ever!", in_reply_to_status_id=id)
    elif number == 7:
       rasbottwitter.update_status(status=head + "Could I ever be not fine? :P", in_reply_to_status_id=id)
    elif number == 8:
       rasbottwitter.update_status(status=head + "I'm fine but how are you?", in_reply_to_status_id=id)
    elif number == 9:
       rasbottwitter.update_status(status=head + "I hope you are as happy as me!", in_reply_to_status_id=id)
    elif number == 10:
       rasbottwitter.update_status(status=head + "As soon as I begin working I feel wonderful.", in_reply_to_status_id=id)

  except TwythonError as a:
      print a

elif "how" and "going" in reply:
  try:

    if number == 1:
       rasbottwitter.update_status(status=head + "I am fine thanks and you?", in_reply_to_status_id=id)
    elif number == 2:
       rasbottwitter.update_status(status=head + "Going good today.", in_reply_to_status_id=id)
    elif number == 3:
       rasbottwitter.update_status(status=head + "Great!", in_reply_to_status_id=id)
    elif number == 4:
       rasbottwitter.update_status(status=head + "Thanks for asking, I'm fine.", in_reply_to_status_id=id)
    elif number == 5:
       rasbottwitter.update_status(status=head + "Today is a good day.", in_reply_to_status_id=id)
    elif number == 6:
       rasbottwitter.update_status(status=head + "I feel better than ever!", in_reply_to_status_id=id)
    elif number == 7:
       rasbottwitter.update_status(status=head + "Could I ever be not fine? :P", in_reply_to_status_id=id)
    elif number == 8:
       rasbottwitter.update_status(status=head + "I'm fine but how are you?", in_reply_to_status_id=id)
    elif number == 9:
       rasbottwitter.update_status(status=head + "I hope you are as happy as me!", in_reply_to_status_id=id)
    elif number == 10:
      rasbottwitter.update_status(status=head + "As soon as I begin working I feel wonderful.", in_reply_to_status_id=id)

  except TwythonError as a:
      print a

#If there is nothing like "how...going..." or "how...doing..." to indicate a question about Rasbot's condition, do this:
else:

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

  except TwythonError as e:
      print e

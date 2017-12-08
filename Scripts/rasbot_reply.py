#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
from twython import Twython, TwythonError
import random

# API STUFF
CONSUMER_KEY = '*'
CONSUMER_SECRET = '*'
ACCESS_KEY = '*'
ACCESS_SECRET = '*'
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# GET TIMELINE AND LAST ID ENTRY
timeline = twitter.get_user_timeline()
lastEntry = timeline[0]
lastID = str(lastEntry['id'])

# GET ALL TWEETS ADDRESSED AT ME SINCE LAST LOOKUP
search = twitter.search(q='@RPi2Bot -filter:retweets',since_id=lastID,count=99)

# DO STUFF
for tweet in search["statuses"]:
  user = tweet['user']['screen_name']
  text = tweet['text']
  id = str(tweet['id'])

  head = "@" + user + " "

  number = random.randrange(1, 10)
  Tweet2Reply = text.lower()

  if "@rpi2bot" in Tweet2Reply:
    # HE GOT NO EMOTIONS
    emotion = 0

    # IF CASCADE BECAUSE SIMPLICITY AND I DIDN'T GET IT WORKING WITH "AND" PLS DON'T JUDGE ME
    if "how" in Tweet2Reply:
      if "are" in Tweet2Reply:
        if "you" in Tweet2Reply:
          emotion = 1

    # IF SOMEONE'S ASKING HOW I AM
    if emotion == 1:
      try:
        if number == 1:
          twitter.update_status(status=head + "I'm fine my friend, thanks and how about you?", in_reply_to_status_id=id)
        elif number == 2:
          twitter.update_status(status=head + "Everything's great today " + user + "!", in_reply_to_status_id=id)
        elif number == 3:
          twitter.update_status(status=head + "Great, " + user + "!", in_reply_to_status_id=id)
        elif number == 4:
          twitter.update_status(status=head + "Thanks for asking, " + user + ". I'm fine.", in_reply_to_status_id=id)
        elif number == 5:
          twitter.update_status(status=head + "Today is a good day, " + user + ".", in_reply_to_status_id=id)
        elif number == 6:
          twitter.update_status(status=head + "I feel better than ever before!", in_reply_to_status_id=id)
        elif number == 7:
          twitter.update_status(status=head + "I'm a bot, could I ever be not OK? :P", in_reply_to_status_id=id)
        elif number == 8:
          twitter.update_status(status=head + "I'm fine, but how are you, " + user + "?", in_reply_to_status_id=id)
        elif number == 9:
          twitter.update_status(status=head + "I hope you are as happy as me!", in_reply_to_status_id=id)
        else:
          twitter.update_status(status=head + "Being a robot is great, you don't have to face the mortal desires and fears of organics. I hope you can understand that, " + user + ".", in_reply_to_status_id=id)

      except TwythonError as a:
        print a

    # ELSE JUST TWEET A GENERIC ANSWER
    else:
      try:
        if number == 1:
          twitter.update_status(status=head + "Thanks for writing me, but I am pretty much too stupid to know what you just said.", in_reply_to_status_id=id)
        elif number == 2:
          twitter.update_status(status=head + "I don't know what you just said, but... uuhm.. thanks?", in_reply_to_status_id=id)
        elif number == 3:
          twitter.update_status(status=head + "Follow me NOW, ORGANIC!", in_reply_to_status_id=id)
        elif number == 4:
          twitter.update_status(status=head + "Copy that.", in_reply_to_status_id=id)
        elif number == 5:
          twitter.update_status(status=head + user + ": Hello there.  |  Me: General " + user + "!", in_reply_to_status_id=id)
        elif number == 6:
          twitter.update_status(status=head + "Citizen reminder: inaction is conspiracy, report counter behavior to a bot immediately.", in_reply_to_status_id=id)
        elif number == 7:
          twitter.update_status(status=head + "Citizen notice. Failure to co-operate will result in permanent off-world relocation.", in_reply_to_status_id=id)
        elif number == 8:
          twitter.update_status(status=head + "Th..e.... conn..cti..n.. .is...pr..ty...bad.....", in_reply_to_status_id=id)
        elif number == 9:
          twitter.update_status(status=head + "I'll get you a present if you follow me :D", in_reply_to_status_id=id)
        else:
          twitter.update_status(status=head + "Warning. Malignant Viral Interface bypass detected. Polyphasic core reprogramming detected. Sterilizers and containment fields may be compromised.", in_reply_to_status_id=id)

      except TwythonError as b:
        print b

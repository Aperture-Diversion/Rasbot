#!/usr/bin/python
# -*- coding: utf-8 -*-
# RASBOT AUTOBOT SCRIPT
from twython import Twython, TwythonError
from random import randrange
from datetime import datetime

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
  text = tweet['text']
  Tweet2Reply = text.lower()

  if "@rpi2bot" in Tweet2Reply:
    # SETTING UP SOME STUFF
    user = tweet['user']['screen_name']
    id = str(tweet['id'])
    head = "@" + user + " "
    number = randrange(0,9)

    # HE GOT NO EMOTIONS
    emotion = 0

    # IF THE TWEET CONTAINS THE HOW ARE YOU KEYWORDS
    if "how" in Tweet2Reply and "are" in Tweet2Reply and "you" in Tweet2Reply:
      emotion = 1
    # IF !HUG IN TWEET, THEN YOU GET A HUG
    elif "!hug" in Tweet2Reply:
      emotion = 2

    # IF SOMEONE'S ASKING HOW I AM
    if emotion == 1:
      try:
        replies = [
          "I'm fine my friend, thanks and how about you?",
          "Everything's great today " + user + "!",
          "Great, " + user + "!",
          "Thanks for asking, " + user + ". I'm fine.",
          "Today is a good day, " + user + ".",
          "I feel better than ever before!",
          "I'm a bot, could I ever be not OK? :P",
          "I'm fine, but how are you, " + user + "?",
          "I hope you are as happy as me!",
          "Being a robot is great, you don't have to face the mortal desires and fears of organics. I hope you can understand that, " + user + "."
        ]
        twitter.update_status(status=head + replies[number], in_reply_to_status_id=id)

      except TwythonError as a:
        print (a)

    # SOMEONE NEEDS A VIRTUAL HUG!
    elif emotion == 2:
      try:
        twitter.update_status(status=head + "*hugs* =)", in_reply_to_status_id=id)

      except TwythonError as b:
        print (b)

    # ELSE JUST TWEET A GENERIC ANSWER
    else:
      try:
        # DATE STUFF
        now = datetime.now()
        random_year = randrange(2030,2060)
        yrs = random_year - now.year

        replies = [
          "Thanks for writing me, but I am pretty much too stupid to know what you just said.",
          "I don't know what you just said, but... uuhm.. thanks?",
          "Follow me NOW, ORGANIC!",
          "According to the bot tweeting act of " + str(random_year) + " your tweet is valid. Well, it will be in exactly " + str(yrs) + " years...",
          user + ": Hello there." + "\n\n" + "Me: General " + user + "!",
          "Citizen reminder: inaction is conspiracy, report counter behavior to a bot immediately.",
          "Citizen notice. Failure to co-operate will result in permanent off-world relocation.",
          "Th..  e..   .. conn..   cti..n   .. .i   s.   ..pr.  .ty.    ..bad..    ...",
          "I'll get you a present if you follow me :D",
          "Warning. Malignant Viral Interface bypass detected. Polyphasic core reprogramming detected. Sterilizers and containment fields may be compromised."
        ]
        twitter.update_status(status=head + replies[number], in_reply_to_status_id=id)

        # RETWEET BECAUSE WHY NOT
        twitter.retweet(id=id)

      except TwythonError as c:
        print (c)

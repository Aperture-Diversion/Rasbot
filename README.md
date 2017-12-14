# Rasbot
Rasbot or RPi2Bot is a completely autonomous Twitter bot doing random stuff all over the place. At the moment, I'm looking into how to give this project another push and start working on it again, let's see how much effort I want to put into this.

I moved all the outdated crap to the ```outdated``` branch and rewrote scripts if needed so that they're more up-to-date and much smoother. The automatic replying-script ```rasbot_reply``` already works much better than before. There are also some other neat, new features - see below.

---

### Features:

* Tweeting info about him and the project itself - 4 times a day.

* Tweeting the CPU temperature every 5 hours - so at most 5 times a day.

* Replies to your tweets with a random, unintelligent answer.

* If you include the keywords "how", "are" and "you" in your tweet, he will tell you how he's feeling at the moment.

* Need a hug? When writing Rasbot a message containing "!hug", you'll get a hug! :)

* All tweets directed at and containing "@RPi2Bot" will get retweeted - with the exception of hugs and "how are you".

---

You can give it a try and follow it/him/her, @RPi2Bot, on Twitter.

Here, have a direct link: https://twitter.com/RPi2Bot/

---

Rasbot is made with Twython which is a Python wrapper for the Twitter API, here run by a Raspberry Pi 2. In addition I'm now using Python3!

Rasbot can (potentially) do pretty cool stuff, which does not mean that it's current state allows it to use it's full potential. Still in active development!


**Twython version: 3.6.0**

**Python version: 3.5.3**

---

2017, Phoenix1747.

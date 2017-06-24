#!/usr/bin/env python

import feedparser
import os

USERNAME = "youremail@gmail.com"
PASSWORD = ""

response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
unread_count = int(response["feed"]["fullcount"])

dir = os.path.dirname(os.path.realpath(__file__))

for i in range(0, unread_count):
  if "[Security-news] Drupal Core" in response['items'][i].title:
    os.system("aplay " + dir + "/alarm.wav")


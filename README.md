# Drupal Core Security Alarm

## Description
This script check the provided email for any unread messages that contain the string [Security-news] Drupal Core. If that string is found the script will play an alarm.

For best results this should be used as a cron task on a raspberry pi that's hooked up to giant speakers.

`* * * * * /path/to/drupal_alert/drupal_alert.py`

## Setup

1. Ensure file is executable `chmod +x drupal_alert.py`

2. Set up python virtual env `virtualenv env`

3. Start the virtual env `source env/bin/activate`

4. Install dependencies `pip install -r requirements.txt`


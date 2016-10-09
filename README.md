# alarm-rasp
Alarm clock scheduled via cron which speaks the weather and news (NPR's RSS feed is default) for your area.

A lot of information and ideas for updates are in DEVNOTES.txt in alarm directory.

####Usage



alarm.config lets you change some things (eg source of news)

To run: 
1) Use cron to schedule alarmMaster.py to run at your desired time. 
2) Hear the news and weather.
3) Edit the source of your news, edit your town for weather, etc., in alarm.config


####Credits
This is based off of skiwithpete's (github.com/skiwithpete) alarm pi project

Uses speech.sh from Dan Fountain (credit is in that file)

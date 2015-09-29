# alarm-rasp
A lot of information is in DEVNOTES.txt in alarm directory
This is based off of skiwithpete's (github.com/skiwithpete) alarm pi project
Uses speech.sh from Dan Fountain (credit is in that file)

Alarm clock which needs to be scheduled via cron (for now) which speaks the weather and the news (currently from NPR's RSS) for your area.

alarm.config lets you change some things (eg source of news) but isn't complete yet

To run: 
1) Use cron to schedule alarmMaster.py to run at your desired time. 
2) Hear the news and weather.
3) Edit the source of your news, edit your town for weather, etc. in alarm.config

# alarm-rasp
All below information is in DEVNOTES.txt in alarm directory
This is based off of skiwithpete's (github.com/skiwithpete) alarm pi project
Uses speech.sh from Dan Fountain (credit is in that file)



To add:
	Truncation of eg wind speed, temperature(78.33333 >> 78)
    	Once Weather can speak, put the speaking in a separate file so all 
speaking can be together eventually
    	Implement wordwrap and counter in speaking section to fit text into 
100 char limit (or don't bc speech.sh)

WEATHERGET:
	Works. 
	Just has humid, wind speed and temp, but it talks. 
	Would like to make things like city and a toggle for humidity, 
precipitation etc to be global (thru alarmConfig)

NEWS:
	Works, but voice is a little wonky
	Will be better if I wrote my own speech.sh, where it breaks at every
period -- this is way better for stuff like news headlines (rather than
just breaking at a space around 100 chars which is what Dan Fountain script
does).

SPEECH.SH:
	Would like to write my own
	Uses mpg123, explanation of flags for speed up/slow down in comments in script
	See "NEWS:" for changes needed

META:
	All things work as of 7/21/15 -- news and weather and cron
	Now to smooth out speech and add functionality to news and weather, as well as add other functions eg 
play music/radio, send text to phone or something, stocks?? BTC??

CRON:
	crontab -e will let you edit cron file and schedule jobs
	using >>alarm.log will put everything printed onscreen into log file

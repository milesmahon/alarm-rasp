# -*- coding: utf-8 -*-
import feedparser #for parsing rss feeds
import subprocess
#import textwrap
import ConfigParser

Config=ConfigParser.ConfigParser()
Config.read('alarm.config')
db=int(Config.get('main','debug'))
main()

def main():
	localFeed = Config.get('news','newsSourceURL')

	rss = feedparser.parse(localFeed)
	newsTitle = Config.get('news','newsSourceTitle')

	count = int(Config.get('news','numArticles'))
	#config seems to assume parameters are strings, so force int

	if (db==1):
		print count + " articles"
		print "from " + localFeed + "\n"
	speak(rss, count, newsTitle)

def speak(rss, count, newsTitle):
	news = "Now the news from " + newsTitle + "... "
	for i in range(count):
		news = news + rss.entries[i]["title"] + ". "

	news = news.encode('utf-8') #otherwise TTS doesn't understand

	if (db==1):
	        print news
	subprocess.call("./speech.sh \"" + news + "\"", shell=True)
#calls TTS script with "news" string from command line

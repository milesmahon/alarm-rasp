# -*- coding: utf-8 -*-
import feedparser #for parsing rss feeds
import subprocess
import textwrap
import ConfigParser

Config=ConfigParser.ConfigParser()
Config.read('alarm.config')

"""Variables--------------------------------------"""

localFeed = Config.get('news','newsSourceURL')

rss = feedparser.parse(localFeed)
newsTitle = Config.get('news','newsSourceTitle')

count = int(Config.get('news','numArticles')) 
#config seems to assume parameters are strings, so force int

db=int(Config.get('main','debug')) 

if (db==1):
	#print count
	#print localFeed
	#print Config.sections()

"""Code--------------------------------------------"""

news = "Now the news from " + newsTitle + "... "

for i in range(count):
	news = news + rss.entries[i]["title"] + ". "

news = news.encode('utf-8')

if (db==1):
        print news

subprocess.call("./speech.sh \"" + news + "\"", shell=True)
#calls TTS script from command line



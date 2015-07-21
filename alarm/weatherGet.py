# -*- coding: utf-8 -*-
import subprocess
import json
import urllib
import urllib2
import ConfigParser

#Reading from Config File -------------------
Config=ConfigParser.ConfigParser()
Config.read('alarm.config')
localCity = Config.get('weather','city')

#Getting weather info -----------------------
weather_api = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + localCity + "&units=imperial")
#can also be done with yahoo weather api

weatherFile = json.loads(weather_api.read())
#convert to JSON readable

temp = weatherFile["main"]["temp"]
humid = weatherFile["main"]["humidity"]
wind = weatherFile["wind"]["speed"]
#snow and rain to be added

#Format weather string -------------------------------
temp = ("Temperature is " + str(temp)+ " degrees. ")
humid = (str(humid) + " percent humidity. ")
wind = ("Wind speed of " + str(wind) + " miles per hour. ")

if (int(Config.get('main','debug')) == 1):
	print temp
	print humid
	print wind

weatherWords = "Today, " + temp + humid + wind


#Speech with google translate ---------------------------

send = ("./speech.sh " + str(weatherWords))
#Using text to speech script (speech.sh) by Dan Fountain, runs through google and
#already accounts for 100 char limit in google voice. genius

subprocess.call(send, shell=True)

#works as of 7/21/15



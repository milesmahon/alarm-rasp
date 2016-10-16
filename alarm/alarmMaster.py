#!/usr/bin/python
import time
import subprocess
import ConfigParser
Config=ConfigParser.ConfigParser()
main()

def main():
	try:
		Config.read('alarm.config')
	except:
		raise Exception("Couldn't connect to alarm config file")

	db = int(Config.get('main','debug'))

	if (db==1):
		print (time.strftime("%d/%m/%Y"))
		print (time.strftime("%I:%M:%S"))
		print ("Alarm start\n\n")

	#uses list of all programs listed in alarm.config
	progList = Config.sections()
	progList.pop(0) #pops "main" because we won't use it here
	run(progList)

"""Start running progs ---------------------------------------"""

def run(progList):
	#subprocess.call("./speech.sh Good morning. ")
	#all files have name format *respective section*Get.py, eg weatherGet, newsGet...
	for x in progList:
		try:
			subprocess.call("python " + x + "Get.py", shell=True)
		except:
			raise Exception("Couldn't retrieve " + x)

	#alternate: call each program to get their return value ( could edit to be a string ), parse it here in this file
	#and send each short sentence to speech.sh so it all flows smoothly and stops at all (". ")'s

	if (db == 1):
		print progList
		print ("Exited successfully\n\n")

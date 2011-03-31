#!/usr/bin/env python 
user = "bill"										#username
password = "llib"									#password
euser = ""											#entered username
epassword = ""										#entered password
while euser != user or epassword != password:
	euser = raw_input("User: ")
	epassword = raw_input("Password: ")
print "Welcome!"
cmd = ""											#makes sure cmd is empty
while cmd != "exit":
	cmd = raw_input(">> ")
	if cmd == "greet":
		print "Hello!"
	elif cmd == "fuck":
		print "Oh yes, do me hard!"
	elif cmd == "rub":
		print "Mmm, rub my cunt!"
	elif cmd == "lick":
		print "Ohh lick my pussy!"
	elif cmd == "exit":
		print "Bye!"
	else:
		print "What?"

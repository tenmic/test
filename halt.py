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
	elif cmd == "sandwich":
		print "Ok, I'll go make you a sandwich."
	elif cmd == "slap":
		print "Ouch."
	elif cmd == "feed":
		print "Yum. Thanks."
	elif cmd == "exit":
		print "Cya!"
	else:
		print "What?"

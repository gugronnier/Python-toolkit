#!/usr/bin/env python

import socket

login="test"
password="xna"
try:
	host=""
	port=12345
	s=socket.socket()
	s.bind((host,port))
	s.listen(1)
	client,ip=s.accept()
	while 1:
		client.send("login : USER <your login>\n")
		print client.recv(1024)
		client.send("password : PASS <your password>\n")
		data=client.recv(1024)
		print data
		if password in data:
			client.send("320 - Connected\n")
		else:
			client.send("530 - Bad password\n")
finally:
	client.close()
	s.close()
	
print "END"



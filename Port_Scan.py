import socket
import subprocess
import sys
from datetime import datetime

scanTarget = raw_input("Enter a remote host to scan: ")
scanIP = socket.gethostbyname(scanTarget)

startPort = raw_input("Enter start port: ")
endPort = raw_input("Enter end port: ")
startPort = int(startPort)
endPort = int(endPort)

print "-"*60
print "Scanning %s and IP Address %s:" % (scanTarget, scanIP)
print "-"*60

t1 = datetime.now()

try:
	for port in range(startPort,endPort):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((scanIP,port))
		if result == 0:
			print "Port %d Open" % port
					
		else :
			print "Port %d is Closed" % port
			
		sock.close()
		
except KeyboardInterrupt:
	print "Scan cancled by CTRL+C press"
	
	
except socket.error:
	print "Couldn't connect to server"
	
	
t2 = datetime.now()

totalTime = t2 - t1

print "Scanning Complete in : ", totalTime

			


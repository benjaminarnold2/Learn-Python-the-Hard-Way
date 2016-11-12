from time import sleep

def start():
	x = True
	y = True
	if (x and y) == True:
		y = False
		print y 

	raw_input()

	while x == True:
		print x 
		sleep (3)
		x = False
	
	raw_input()
	
	if (x or not y) == True:
		print x,y 
	
	raw_input()
	
	global s
	print s
	
	s = "Local!"
	
	print s
	
	raw_input()
	
	mygenerator = (1,2,3)
	mylist = [1,2,3]
	for i in mygenerator:
		print i 
	raw_input('g')
	for i in mylist:
		print i 
	raw_input('l')
	for i in mygenerator:
		print i 
	raw_input('g')
	for i in mylist:
		print i
	raw_input('l')
	
s = "Global"
start()
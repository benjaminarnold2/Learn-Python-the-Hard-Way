from sys import exit

def int_finder(number):
	try:
		int(number)
		return True
		
	except ValueError:
		return False

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input('>')
	value = int_finder(next)
	if value == True:
		how_much = int(next)
	else: 
		print "Man, learn to type a number."
		gold_room()
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("Dude, way to be greedy!")
	
		
def bear_room():
	print """
		There is a bear in here. The bear has a bunch of honey.
		The fat bear is in front of another door. 
		How are you going to move the door? 
		"""
	bear_moved = False
		
	while True:
		next = raw_input(">")
			
		if "take" and "honey" in next:
			dead("The bear slaps your face off!")
		elif "taunt" in next and not bear_moved:
			print "The bear has moved. You are free to go!"
			bear_moved = True
		elif "taunt" in next and bear_moved:
			dead("The bear didn't like that, and chewed your butt off!")
		elif "open" and "door" in next and bear_moved:
			gold_room()
		else:
			print "I have no idea what you just did"
			bear_room()
				
def cthulhu_room():
	print """
	Here you see the dreaded Cthulhu. 
	He stares at you and you start to go crazy!
	Do you run away, or start to sing show tunes?
	"""
	
	next = raw_input('>')
	
	if "run" in next:
		print "You made it out safe, although you kind of think that you're a banana."
		start()
	elif "sing" in next:
		dead("Well, now you're crazy!")
	else: 
		print "That was a little too crazy!"
		cthulhu_room()
		
def dead(why):
	print why, "God job tard! Try again!!"
	start()
	
def start():
	print """
	You are in a dark room. There is a door to your right and left.
	Why are these rooms always dark? 
	Screw that... you're in a sunny nice room.
	There are two very nice doors to your right and left.
	What are you going to do buddy? 
	"""
	
	next = raw_input('>')
	
	if "left" in next:
		bear_room()
	elif "right" in next:
		cthulhu_room()
	else:
		print "That's a bold strategy Cotton"
		print "Let's see if it pays off for him."
		start()
				
start()
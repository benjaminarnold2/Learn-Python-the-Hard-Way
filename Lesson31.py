print "You enter a dark room with two doors. DO you go through door #1 or door #2?"

door = raw_input(">")

if door == "1":
	print "There is a giant bear here eating a cheese cake!"
	print "What are you going to do, buddy?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input(">")
	
	if bear == "1":
		print "The bear eats your face off. You don't mess with bears!"
	elif bear == "2":
		print "The bear screams back at you, chokes on the cake and dies!"
		print "You take the cake and get fat."
		print "You can't fit back through the door... so you're stuck forever."
	else:
		print "Yeah, well since %s isn't option one or 2, you failed to do anything." % bear
		print "In your moment of indecision, the bear decides that you'd make a great scratching post."
		print "You died  by being scratched to death by a cheese cake eating bear."
elif door == "2":
	print "Behind door #%s, you find the dark god Cthulhu, destroyer of worlds!"
	print "You stare into the endless abyss of Cthulhu's gaze and slowly go crazy."
	print """
	What's your plan now? \n
	1. "All my best friends are blueberries!"
	2. "Watermelons are the laziest of all fruits!"
	3. "I can fart the theme song to Adventure Time!"
	"""
	insanity = raw_input(">")
	
	if insanity == "1":
		print "Your mind has turned to jello. You are now as smart as Momo. You spend the rest of your life licking small rocks."
	elif insanity == "2":
		print "Thinking quickly, you decide to blame watermelons for your laziness. Unfortunatly, Cthulhu's best friends are watermelons."
		print "You have angered the dark god Cthulhu, which is a pretty dumb move. He mushes you into a fine paste and brushes his teeth with it. Ewww..."
	elif insanity == "3":
		print "Cthulhu loves Adventure Time! You guys become friends and share some great adventures together. Turns out Cthulhu isn't such a bad evil world destryoing god after all!"
	else:
		"You choose to do nothing. Cthulhu doesn't like this and turns you into a tatter tot. Mom feeds your tatter tot body to Whiskey, who throws it up on the rug."
else:
	print "In a bold move, you decide to do %s instead. You run full speed into a wall and knock yourself out and die. You are the worst adventure ever." % door
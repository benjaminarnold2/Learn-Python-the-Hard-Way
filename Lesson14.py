from sys import argv

script, user_name = argv
prompt = '>>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like it in the butt %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking it in the butt.
You live in %r. I think that place sucks.
You also have a %r computer. 
Fan-fucking-tastic!
""" % (likes, lives, computer)


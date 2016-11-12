ten_things = "Apples Oranges Crows Telephones Light Sugar"

print "Wait, there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some stuff with stuff."

print stuff[1]
print stuff [-1] #will this print zero?
print stuff.pop()
print ' '.join(stuff) #adds a space for each entry?
print '#'.join(stuff[3:5]) #adds # at 3 through 5?
print stuff[3:5]
thing = ' '.join(stuff)
print thing
print stuff

print isinstance(thing, str)
print isinstance(stuff, str)

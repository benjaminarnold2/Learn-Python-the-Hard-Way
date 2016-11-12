def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b 
	
def multiplying(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b 
	
def dividing(a, b):
	print "Dividing %d * %d" % (a, b)
	return a / b 
	
print "Let's do some math with just functions!!"

age = add(30, 8)
height = subtract(79, 6)
weight = multiplying(95, 2)
iq = dividing(300, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiplying(weight, dividing(iq, 2))))

print "That becomes: ", what, " - Math bitches!!"
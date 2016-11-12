print "Let's practice everything!"
print 'You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs.'

poem = """

\tThe lovely world
with logic so firmly planted
cannot disern \n the needs of love
nor compreehnd passion from intuition
and requires an explaination
\n\t\twhere there is none. 
"""

print "-" * 40
print poem
print "-" * 25

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	

start_point = raw_input("Enter the seed number for jelly beans: ")
start_point = int(start_point)
beans, jars, crates = secret_formula(start_point)

print beans, jars, crates

print "With a seed number of %d " % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do it this way: ", "We'd have %s beans, %d jars, and %s crates" % secret_formula(start_point)





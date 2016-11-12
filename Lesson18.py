def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "We ain't found shit!"
	
print_two("Ben", "Arnold")
print_two_again("Max", "Power")
print_one("Beans!")
print_none()


i = 0
numbers = [] #empty list

def counter(number):
	print "i is now %d" % number
	numbers.append(number)
	print "numbers list is now ", numbers
	number += 1
	print "i is now %d" % number
	return number

while i < 6: #should run 6 times 0 - 5
	i = counter(i)
	#print "At the top i is %d" % i
	#numbers.append(i) # fills the list
	
	#i += 1
	#print "Numbers now: ", numbers
	
	#print "At the bottom of this while loop i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num
	
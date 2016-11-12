the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#The third loop has both strings and ints in it. 

for number in the_count:
	print "This is the count %d." % number
	
for fruit in fruits:
	print "Here are some %s." % fruit
	
for i in change:
	try:
		print "I have %d." % i
		
	except TypeError:
		print "I have %s." % i 
		
	
elements = []

#empty list

for i in range(0,6):
	print "Adding %d to the list." % i
	#append to list
	elements.append(i)

for i in elements:
	print "elements was: %d." % i 
	

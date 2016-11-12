def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "You fat bastard!"
	print "Time to go to the gym!\n"
	
print "We can just give the function numbers directly: "
cheese_and_crackers(20, 30) #this is just calling the function in the code

print "Or, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#calling the function and passing varaibles with values inserted

print "We can even do some math when calling the function"
cheese_and_crackers(10 + 20, 5 + 6)
#python will resolve the math when calling the function

print "We can even do math against the variables we set"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


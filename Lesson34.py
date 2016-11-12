#quick loops

def shiny(num):
	redrum = 'MURDER!'
	while num > 0: 
		print "All work and no play makes Ben a dull boy."
		num = int(num)
		num = num - 1
	return redrum

print '-' * 30
print "Here's a quick loop"

repeat = raw_input("Enter the amount of times you want the loop to loop!: > ")

mystery = shiny(repeat)

print mystery


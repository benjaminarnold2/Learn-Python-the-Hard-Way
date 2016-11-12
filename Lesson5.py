my_name = 'Benjamin Arnold'
my_age = 38
my_height = 73.0
my_weight = 195.0
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are %s." % my_teeth

weight_kilo = my_weight * 0.45359237
height_cent = my_height * 2.54
height_feet = float(my_height / 12.000)

print "If I add %d, %d, and %d together, I'd get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "weight in kilos is %r" % weight_kilo
print "height in centimeters is %d" % height_cent
print "Height in feet is ", height_feet
print height_cent


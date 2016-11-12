from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)."
print " If you do want to do that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a+')
old = target.read()
target.seek(0)
print old

print "Truncating the file. Goodbye!"
target.truncate()

#print original

print "Now we'll add three lines back to the file"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
space = "\n"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "Do you want to save your file?"

answer = raw_input("Type yes or no: ")
proceed = "yes"

if answer == proceed:
	target.close()
else:
	print "Locating read/write pointer in file"
	print "Read/write pointer is at byte %s." % target.tell()
	print "Moving to begining of file..."
	target.seek(0)
	print "Locating read/write pointer in file"
	print "Read/write pointer is now at byte %s." % target.tell()
	target.truncate()
	target.write(old)
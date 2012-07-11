# Exercise 16

# this is a very simple text editor to practice file manupulation commands

# import the argv module from the sys module
from sys import argv

# unpacks the argv into script and filename
# 'script' indicates the program itself. 'filename' is a string that here takes the name of an existing .txt file or creates one if it does not exist. 
# the variables after 'script' must be spplied AT THE COMMAND LINE
script, filename = argv

# the variable here is the name of the file supplied at the command line
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# this pauses the program to take input from the user. really, it doesn't matter what you put in here--it's just giving you the chance to proceed by hitting enter or terminate the program with ^C.
raw_input("?")

# open takes that parameters (file, mode); here 'w' mode is for writing. target is just the target file.
print "Opening the file..."
target = open(filename, 'a')

# this truncates or erases the file.
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

# take three piees of raw input and assign each to a variable. the paramater for 'raw_input' here is the promt that will be displayed.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# again, 'target' is the object holding the file that got opened above. this writes the value of each 'line' variable into the contents of the file, with a "\n" (line break) written in between each.
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# This does the same thing as above, but is more terse.
lines = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(lines)

# obvi.
print "And finally, we close it."
target.close()
# read: a simple reader script to check the contents of files created or modified for other exercises.

# import the argv module from the sys module
from sys import argv

# unpacks the argv into script and filename
script, filename = argv

# opens the file passed from argv as 'filename' and sets the contents as variable 'txt'
txt = open(filename)

print "Here are the contents of the file %r:" % filename
print "_BEGIN_" + "\n"
# takes the contents of the file set as variable 'txt' and reads the content with no parameters
print txt.read()
print "\n" + "_END_" + "\n"

# close the open file
txt.close()
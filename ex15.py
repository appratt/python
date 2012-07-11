# Exercise 15

# import the argv module from the sys module
from sys import argv

# unpacks the argv into script and filename
script, filename = argv

# opens the file passed from argv as 'filename' and sets the contents as variable 'txt'
txt = open(filename)

print "Here's your file %r:" % filename
# takes the contents of the file set as variable 'txt' and reads the content with no parameters
print txt.read()

# asks for raw input and takes the filename again, setting the filename as variable 'file_again'
print "Type the filename again:"
file_again = raw_input(">")

# opens the file passed from raw_input() as 'file_again' and sets the contents as variable 'txt_again'
txt_again = open(file_again)

# takes the contents of the file set as variable 'txt_again' and reads the content with no parameters
print txt_again.read()

# close the open files
txt.close()
txt_again.close()
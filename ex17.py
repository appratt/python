# Exercise 17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# merge these into one line:
# input = open(from_file)
# indata = input.read()

# this syntax is totally wrong...how to combine? another function that opens + reads?
indata = from_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CNTRL-C to abort."
# raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright; all done."

output.close()
input.close()
# Exercise 11

# Time for some input!
# I am assuming that raw_input() can take any sort of string and treats it as a string

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
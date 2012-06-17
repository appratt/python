# Exercise 6

# %d here is data or a number value representing the possible types of people
x = "There are %d types of people." % 10

# variables that are their own names as a strings
binary = "binary"
do_not="don't"

# places the strings defined above into a sentence
y = "Those who know %s and those who %s." % (binary, do_not)

# prints that sentence
print x
print y

# repeats the above results but demonstrates the properties of single and ounble quate snytax
print "I said: %r." % x
print "I also said: '%s'," % y

# set value of funny variable
hilarious = False
# evaluates joke by displaying evaluation qustion and value of funny variable
joke_evaluation = "Isn't that joke so funny?! %r"

# prints results of the above
print joke_evaluation % hilarious

# two strings that are clauses in a sentence
w = "This is the left side of..."
e = "a string with a right side."

# combine the clauses and print the sentence
print w + e
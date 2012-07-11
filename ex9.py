# Exercise 9

# This is some new stange notation. Watch for typoes.

days = "Mon Tue Wed Thu Fri Sat Sun"
# the \n escape character inserts a line break before the next value
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

# tripple quotes allow for free text, a-la the '<pre>' tag in HTML. '\n' still works within this text
print """
There's soomething going on here,\n\n
With the three double-quotes. But does it 'work' like "this"?
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
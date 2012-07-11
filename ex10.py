# Exercise 10

# more experimentation with excape characters and getting quotes into strings

# \t inserts a Tab character
tabby_cat = "\tI'm tabbed in."
# \n inserts a line break character
persian_cat = "I'm split\non a line."
# \\ escapes the backclash so that the backslash becomes part of the string
backslash_cat = "I'm \\ a \\ cat."

# the \t insert tabs for the list; the final line is just a messy (or condensed?) way of inserting the line break that would otherwise be created in this code
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

fat_cat2 = '''
"I'll" do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

format_cat = "I'm a %s cat." % '\nmagic\n'

print "now for fat cat 2 & extra credit"
print fat_cat2
print format_cat
# Exercise 5

name = "Andrew Pratt"
age = 29 # Yes indeed!
height = 71.0000 # inches
weight = 145 # lbs
eyes = "Blue"
teeth = 'White'
hair = 'Blonde'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He weights %d pounds." % weight
print "Lithe, I know."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this one is tricky
print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)

print "For someone %r inches tall, his hair is awfully %s." % (height, hair)


# converstions
height_metric = height*0.0258 # meters
print "%s is %d inches tall, but in France that would be %d meters." % (name, height, height_metric)
# Exercise 4

# total number of cars
cars = 100
# spots in each car--floating point so that remainders are obvious
space_in_a_car = 4.0
# number of people who can drive
drivers = 30
# total number of people who need a drive
passengers = 90
# subtract the number of total cars from the number of drivers to get the number of cars not driven
cars_not_driven = cars - drivers
# the number of cars driven equals the number of drivers
cars_driven = drivers
# total number of passangers possible in the carpool is cars drive times capacity per car
carpool_capacity = cars_driven * space_in_a_car
# the average number of passangers in each car is the total number of passengers divided by the number of cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
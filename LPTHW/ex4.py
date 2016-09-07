#To begin, we will identify the numbers of each variable:
#The number of cars available:
cars = 100

#Passenger capacity of each car:
space_in_a_car = 4.0

#Number of drivers offering their car:
drivers = 30

#Number of people who need to carpool:
passengers = 90

#The number of cars not driven:
cars_not_driven = cars - drivers

#The number of drivers is defined by each individual car being driven:
cars_driven = drivers

#The carpool capacity is defined by the number of cars multipled by the available spaces in each car:
carpool_capacity = cars_driven * space_in_a_car

#The number of individuals carpooling (passengers) divided by the number of cars available:
average_passengers_per_car = passengers / cars_driven

#In English, we describe the resources available for carpooling:
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

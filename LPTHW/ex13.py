from sys import argv
#Here we import a module from sys to keep code small.
#argv is the "argument variable" which holds arguments you pass to Python script
#when you run it.

script, first, second, third = argv
#Assigning argv to four variables to unpack argv in each variable

print "The script is called: ", script
print "The first variable is:", first
print "The second variable is: ", second
print "The third variable is: ", third

#If we run the script with too few parameters, the remaining arguments are not
#defined. As long as argv is set to some variables, each variable must have set parameters.

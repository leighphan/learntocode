from sys import argv
#import allows you to import Python modules
#argument variable holds the arguments you pass to your Python script when you run it.

script, first, second, third = argv
#this line 'unpacks' argv so instead of holding all arguments, it gets assigned to four variables you can work with

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

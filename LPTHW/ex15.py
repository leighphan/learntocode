from sys import argv
# From the 'sys' module, we import 'argv', which is chosen from a list of CLI arguments.

script, filename = argv
# Defining the list of arguments for 'argv', script name comes first;
# which is also counted in number of args.
# Args are listed in the order in which we define it.

txt = open(filename)
# The object 'txt' will open a file, and user will enter a filename.
# This will create a file object - like a container/reader for file contents.

print "Here's your file %r:" % filename
# Takes input (filename) from user
print txt.read()
# We call a function on the object ('txt') by appending a dot (.), telling
# it to read (with no parameters).
# For a list of available functions on this object, we can type:
# print dir(txt)

print "Type the filename again:"
file_again = raw_input("> ")
# Create a variable called "file_again" which prompts the user for raw input.
txt_again = open(file_again)
# Create a variable called "txt_again" which creates an object file to open
# the parameter called "file_again".

print txt_again.read()
# Here we call a function ("read") on the object txt_again, commanding
# the program to read the contents of "txt_again".

print "Close the file"
file_again = raw_input("> ")

txt_again = file_again.close()

from sys import argv
# From the 'sys' module, we're importing the 'argv' variable

print argv
script, filename = argv
# When defining parameters for argv, always includes 'script, ...'
# Why can't we define 'argv' first, such as 'argv = script, filename'??
txt = open(filename)
# print dir(txt)
# The object 'txt' will open a file; the user will enter filename. Creates
# a file object, which is similar to a container/reader for the contents.

print "Here's your file %r:" % filename
# Here we'll print the text, including a filename entered raw by user
print txt.read()
# What does this mean? The script calls a function on 'txt' which opens
# a file. Where does the "read" portion come from?
# *** You give a file a command by running the dot (.), the name of command,
# and the parameters. In this case, we tell 'txt' to do its command ('read')
# with no parameters.
# How do we know which commands are available?

print "Type the filename again:"
file_again = raw_input("> ")
# Create variable called 'file_again' which prompts user for raw input.
text_again = open(file_again)
# Create variable called 'text_again' which opens the filename the user enters.
print text_again.read()
# Print 'text_again' which opens the file input by user, and read the file.

# Opening and reading a file using the 'argv' variable seems like
# a better way to open and read files since the 'sys' module offers a list
# of command line tools under the module, allowing for more flexibility.
# In the second script, the user must enter the filename more than once.

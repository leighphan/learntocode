x = "There are %d types of people." % 10
# Assign the variable x to a value, which includes a modulo operator (10).

binary = "binary"
# Assign the variable binary to the word "binary"

do_not = "don't"
# Assign variable do_not to its English contraction.

y = "Those who know %s and those who %s." % (binary, do_not)
# Assign variable y to a value, which includes a list of modulo operator values. We reference previously-defined variables on the list.

print x
print y

print "I said: %r." % x
# The interpolation operator '%r' displays raw data of a variable; commands program to 'print no matter what.'
print "I also said: '%s'." % y
# Printing the statement with '%s' returns the value we assigned within the double-quotes.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# We assign variables for the follow-up question

print joke_evaluation % hilarious
# Here, we print the value of variable 'joke_evaluation' and return the value of variable "hilarious".

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# We join the variables 'w' and 'e' with a '+' to connect the strings.
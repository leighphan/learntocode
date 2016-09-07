formatter = "%r %r %r %r"
# Assign variable 'formatter' with value of string of repeated '%r'.

print formatter % (1, 2, 3, 4)
# Printing the variable 'formatter' with string formatted to take values '1, 2, 3, 4'

print formatter % ("one", "two", "three", "four")
# Printing variable 'formatter' with string formatted to take values 'one', 'two', etc.

print formatter % (True, False, False, True)
# Printing variable 'formatter' with values of 'True' and 'False'.
# Since values are not enclosed within double-quotes, they are not strings.


print formatter % (formatter, formatter, formatter, formatter)
# In this line, the 'formatter' variable is embedded as the 'formatter' values.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

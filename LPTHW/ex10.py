tabby_cat = "\t'I'm tabbed in.'"
#Define variable 'tabby_cat' including' '\t' which tabs in the printed value.

persian_cat = "I'm split\non a line."
#Define variable 'persian_cat' including '\n' which starts new line wherever it is typed.

backslash_cat = "I'm \\ a \\ cat."
#Define variable 'backslash_cat' including double backslash to escape spaces.

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#Triple quotes (double or single) allows you to type multiple lines.
#We include horizontal tabs (TAB) to tab in the list items.
#Backslash n (\n) creates ASCII linefeed

#In programming, formatting and escape sequences allow you to style code.
#For example, escape sequences like '\t' let you tab a line of text:

print """
In programming, you can adjust formatting and style of text. For example:
%s
""" % tabby_cat

print """
You can also perform carriage returns, or new lines. For example:
'%r'
will return
'%s'.
""" % (persian_cat, persian_cat)

print """
With escape characters such as double backslash, you can escape
using backslash within the string and to escape as in the following:
%s
""" % backslash_cat

print """
You can also create a list using new lines and tabbing. For example,
'%r'
would return
'%s'
""" % (fat_cat, fat_cat)
from sys import argv

script, user_name = argv
# Here, argv requires the user to enter 'user_name' in order to run the script.
prompt = '> '
# Prompt is set to the value of a string, identified by a simple '> '.

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)
# Here we set the varible value for 'likes' to equal whatever the user
# enters as an answer to the prompt. What is the best Python syntax
# in this situation? Is it best practice to also keep comments under 80 chars?
# *** CORRECTION: https://www.python.org/dev/peps/pep-0008/#block-comments
print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What programming language are you learning?"
language = raw_input(prompt)
print "What do you want to do with %s?" % language
project = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
You said you want to %r with %r.
""" % (likes, lives, computer, project, language)
# Again we input the answers entered by the user to replace %r (representation).
# The %r takes the value of each prompt; we list the variables after the '%'
# in order to complete the string.

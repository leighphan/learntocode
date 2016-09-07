print "To whom are we addressing the letter?"
name = raw_input()
print "How should we start our letter?"
salutation = raw_input()
#"Happy birthday!"
print "What activity do you look forward to this summer?"
road = raw_input()
#"taking road trips together"
print "What activity involves two wheels?"
bike = raw_input()
#"long bike rides"
print "What do we like to do on our walks?"
walk = raw_input()
#"smelling all the flowers on the way home"


print "Dear %r," % name
print "Happy birthday! This year I look forward to many adventures with you, including",
"%s," % raw_input(road), "%s," % raw_input(bike), "and %s." % raw_input(walk)
print "I hope you have the best birthday ever, and that I can share it with you."
print "Love always, Leigh"

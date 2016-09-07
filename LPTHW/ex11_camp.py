print "In which city is the cabin?"
city = raw_input()
print "How many miles away is the cabin?"
distance = int(raw_input())
print "What is the speed limit on I-5?"
mph = int(raw_input())

travel_time = (distance / mph)

print """
  The cabin is in %r. Since it is %r miles away, and we drive %r miles
  per hour, it will take us %r hours to get to the cabin.
  """ % (city, distance, mph, travel_time)

pints = float(input("How many pints have you had? "))

if pints > 2:
    print "You cannot drive a car!"
    if pints > 6:
        print "Call a cab!"
    else:
        print "Ride your bicycle!"
elif pints > 0:
    print "Drive very cautiously!"
else:
    print "It is ok to drive!"

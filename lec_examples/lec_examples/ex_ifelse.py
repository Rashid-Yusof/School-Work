try:	
	number = float(input("Enter a number: "))

	if number > 0:
    	print("It is positive.")
	else:
    	print("It is not positive.")
finally:
	print "That is not a number."

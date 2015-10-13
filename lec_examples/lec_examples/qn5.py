string = "The 2nd chapter has 12 pages."
letters = 0
digits = 0
for ch in string:
	if ch.isalpha():
		letters += 1
	elif ch.isdigit():
		digits += 1

print ("Letters: ", letters)
print ("Digits: ", digits)

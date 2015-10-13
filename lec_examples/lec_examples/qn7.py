word = input("Type a word/sentence to check if it is palindromic! ")
nospace = word.replace(" ","")
reverse = nospace[::-1].lower()
print (reverse,nospace.lower(),word)

if reverse == nospace.lower():
	print ("It's Palindromic!")
else:
	print ("It's not Palindromic, sorry!")

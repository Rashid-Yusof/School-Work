total = 0
count = 0
while True:
	try:
		num = input("Enter a number: ")
		count += 1
		total += int(num)
		print (count)
	except ValueError:
		if num == "":
			if count != -1:
				print (total/count)
				break
		else:
			print ("Please enter a number.")
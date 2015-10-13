import random
number = random.randrange(1,11)
while True:
	guess = int(input("Guess the number (from 1-10)!: "))
	if guess == number:
		print ("Correct!")
		break
	elif guess > number:
		print("That's too high.")
	else:
		print("That's too low.")
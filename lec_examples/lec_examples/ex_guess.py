number = 20

guess = int(input('Enter a number: '))

if guess == number:
    print('Congratulations, that is correct!')
elif guess < number:
    print('No, it is bigger than that.')
else:
    print('No, it is smaller than that.')

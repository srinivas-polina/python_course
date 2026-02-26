import random
roll = random.randint(1,6)

guess = int(input("Guess the number on the dice (1-6): \n"))

if guess == roll:
    print("Congratulations! you guessed the correct number, They rolled a" + str(roll))
else:
    print("Sorry!, computer rolled " + str(roll))
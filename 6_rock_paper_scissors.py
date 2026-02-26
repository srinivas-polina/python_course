


#letting computer have a randomized choice each time we run the program.
#we can use the random module to generate a random

import random

computer_choice = random.choice(["rock","paper","scissors"])
user_choice = input("Enter your choice (Rock, Paper, Scissors): \n")

if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win!")
else:
    print("Computer Win, You Lost!, computer choose", computer_choice, "You choose", user_choice)
# we are going to create a basic dice game where two users will roll pair of dice to see who wins.
import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint (1, 6)
    return dice_total

def main():
    player1 = input("Enter player 1's Name: \n")
    player2 = input("Enter player 2's Name: \n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print("Player 1 rolled: ", roll1)
    print("Player 2 rolled: ", roll2)

    if roll1 > roll2:
        print("Player 1 wins!")
    elif roll2 > roll1:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

main()
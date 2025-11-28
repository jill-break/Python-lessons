import random


def roll_dice():
    print("(", random.randint(1, 6), ",", random.randint(1, 6), ")")


print("Dice Rolling Game")
roll = input("Eenter 'roll' to Roll the dice: ")

if roll.lower() == "roll":
    roll_dice()
    q = input("Roll the dice? (y/n): ")
    while q == "y":
        roll_dice()
        break

elif roll.lower() == "exit":
    exit()
else:
    print("Wrong input! try again")

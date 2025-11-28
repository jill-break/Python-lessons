import random

def game(secret_number, number_of_guesses):
    while number_of_guesses > 0:
        guess = int(input("Enter your Guess: "))
        if guess == secret_number:
            print("Congratulations you got it")
            break
        elif guess > secret_number:
            print("too high")
        elif guess < secret_number:
            print("too low")
        
        number_of_guesses -=1
        print(f"Guesses left: {number_of_guesses}")
    if number_of_guesses == 0:
        print(f"Out of guesses! The number was {secret_number}")


def easy():
    print("Guess the number (between 1 and 5): ")
    secret_number = random.randint(1, 5)
    game(secret_number, 3)


def medium():
    print("Guess the number (between 1 and 15): ")
    secret_number = random.randint(1, 15)
    game(secret_number, 5)


def hard():
    print("Guess the number (between 1 and 50): ")
    secret_number = random.randint(1, 50)
    game(secret_number, 10)


def expert():
    print("Guess the number (between 1 and 100): ")
    secret_number = random.randint(1, 100)
    game(secret_number, 20)


print("Welcome to to the guessing game")
level = int(input("Select Level \n 1 : Easy \n 2 : Medium \n 3 : Hard \n 4: Expert \n => "))

if level == 1:
    print("The Easy Level")
    easy()
elif level == 2:
    print("The Medium Level")
    medium()
elif level == 3:
    print("The Hard Level")
    hard()
elif level == 4:
    print("The Expert Level")
    expert()
else:
    print("Invalid")


# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit

import random

def you_guess():
    number = random.randint(1, 100)
    print("I'm thinking of a number 1-100")
    player_guess = int(input("your guess: "))
    while player_guess != number:
        if player_guess > number:
            print("too high! try again")
            player_guess = int(input("new guess: "))
        elif player_guess < number:
            print("too low, retry")
            player_guess = int(input("new guess: "))
    if player_guess == number:
        print(f"spot on! my number was indeed {number}!")

def i_guess():
    upperbound = 101
    lowerbound = 0
    print("think of a number 1-100")
    comp_guess = random.randint(lowerbound, upperbound)
    print(f"my first guess is {comp_guess}")
    info = input("is your number higher lower or correct: ")
    while info != "correct":
        if info == "higher":
            lowerbound = comp_guess
            comp_guess = random.randint(lowerbound+1, upperbound-1)
            print(f"my next guess is {comp_guess}")
            info = input("is your number higher lower or correct: ")
        elif info == "lower":
            upperbound = comp_guess
            comp_guess = random.randint(lowerbound+1, upperbound-1)
            print(f"my new guess is {comp_guess}")
            info = input("is your number higher lower or correct: ")
    #if info == "correct":
    print("horray!")


print()
print()
game = input("would you like to guess or me to guess: ")
if game == "me":
    you_guess()
elif game == "you":
    i_guess()
print()
print()
"""A number-guessing game."""

print('Good day, challenger. Do you feel lucky?')


get_name = input("Enter your name, if you dare to continue:")


print("Be prepared to lose,", get_name)


def get_user_input():
    guess = -1
    try:
        guess = int(input("Enter a number from 1 to 99: "))
    except ValueError: 
        print("Your guess must be a valid base 10 integer")
    return guess


import random
n = random.randint(1, 99)
guess = get_user_input()
while n != guess:
    print
    if guess < n:
        print ("Too low, try again!")
        guess = get_user_input()
    elif guess > n:
        print ("Too high, try again!")
        guess = get_user_input()
    

print("This is not possible! No mere mortal can defeat me! It must be a fluke. Or did you cheat, " + get_name + "?")
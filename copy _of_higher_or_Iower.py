from random import randrange
import random

guess = int(input("Enter number between 1 and 10: "))
ran_num = random.randint(1, 10)

while ran_num != guess:
    if guess < ran_num:
        print("too low")
        guess = int(input("Enter number between 1 and 10: "))
    elif guess > ran_num:
        print("too high")
        guess = int(input("Enter number between 1 and 10: "))
    else:
        print("your guess is correct")
        break

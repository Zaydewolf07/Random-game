import random

number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9 or perish")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congragulations you shall not die today")
        break
    elif guess < number:
        print("Your guess was too low, think higher")
    elif guess > number:
        print("Your guess was too high, think lower")
    chances = chances + 1
if not chances < 5:
    print("Mwahaha, you did not pass. DIE MORTAL")
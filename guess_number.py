import random

def randnum(x):
    random_number = random.randint(1, x)
    randnum = 0
    while randnum != random_number:
        randnum = int(input(f"Guess a number between 1 and {x}: "))
        if randnum > random_number:
            print("You guessed too high.")
        elif randnum < random_number:
            print("You guessed too low")
            
    print("You are correct")
        
randnum(20)
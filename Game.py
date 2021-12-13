import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a number between 1 to 9")
while chances < 5 :
    guess=int(input("Enter your guess:"))
    if guess== number :
        print("CONGRATULATIONS you won !!")
        break
    elif guess< number :
        print ("Sorry, your guess was too low :(",guess)
    else:
        print ("Sorry, your guess is too high :(",guess)    
    chances=chances+1
if not chances < 5 :
    print("You lose !! The number is",number)
    

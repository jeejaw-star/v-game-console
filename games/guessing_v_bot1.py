import random
def play():
    number=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100. I'll give you 10 tries.")
    tries=0
    while tries < 10:
        guess=int(input("What's your guess?\n"))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You got it!")
            return True
        tries+=1
    return False
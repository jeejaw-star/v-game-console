import games.guessing_v_bot1
from users import *
def main():
    games_costs={"guessing game against bot":10}
    user=User()
    if user.logged_in:
        pass
    else:
        while not user.logged_in:
            user=User()
    while True:
        print("What game do you want to play?")
        game=input("1: Guessing game where you guess a number a bot is thinking of. Cost: 10 credits\n"
        "2: Exit\n")
        if game == "1":
            if user.credits >= 10:
                user.credits-=10
                if games.guessing_v_bot1.play():
                    user.credits+=10
                    print("Congratulations! You got 10 credits!")
            else:
                print("You don't have enough credits for that. Try some of the free games to earn some!")
        elif game == "2":
            print("See you later!")
            return 

if __name__ == "__main__":
    main()  
    
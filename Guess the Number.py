    import random

num = random.randint(0,15)

guess = int(input("Let's Play a Game..! Guess the Number which i think...? The Range between (1 - 15) : "))

while num!=guess :
    if guess>num:
        print("Your Guess is High..")

    else :
        print("Your Guess is Low..")

    guess = int(input("Guess Again....!"))

print("You Won")

# Random number generator program for tossing the coin

import random

print("Welcome to Random Coin Toss Game")
dec = int(input("Enter 1 for coin toss and 0 to exit\n"))
if dec == 1:
    rand = random.randint(0,1)
    if rand == 0:
        print("Head")
    else:
        print("Tail")
else:
    exit()
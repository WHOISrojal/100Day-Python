# Easy game using if else statement
print("Welcome to Treasure Island. Your mission is to find the treasure")

dec = input("Do you want to go left or right?")
if dec == "left":
    dec1 = input("Do you want to swim or wait?")
    if dec1 == "wait":
        dec2 = input("Which color door will you choose?")
        if dec2 == "yellow":
            print("You win")
        else:
            print("Gameover")
    else:
        print("Gameover")
else:
    print("Gameover")
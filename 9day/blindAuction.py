# A blind auction program to determine who is the highest bidder
import os
from art import logo

def clear_screen():
    if os.name == 'posix':  # Unix/Linux/Mac OS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

bids = {}
bidding_finished = False

def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

print(logo)
print("Welcome to the secret auction program")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price  
    should_continue = input("Are there any other bidders? 'yes' or 'no'")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()
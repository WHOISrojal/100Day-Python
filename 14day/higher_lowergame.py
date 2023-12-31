import random
from gamedata import data, logo, vs
import os

def clear_screen():
    if os.name == 'posix':  # Unix/Linux/Mac OS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue == True:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("\nWho has more followers 'A' or 'B':").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear_screen()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}")
    else:
        game_should_continue = False
        print(f"You're wrong. Final score: {score}")




    
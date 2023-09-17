from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You guessed it right. The answer was {answer}\n")
        decision = input("Do you want to restart the game from start? 'yes' or 'no'\n")
        if decision == 'yes':
            return game()
        else:
            print("Bye Bye Have a nice day")
            return
        
def set_difficulty():
    level = input("Choose a dificulty 'easy' or 'hard':\n")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number\n")
        guess = int(input("Make a guess\n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses\n")
            
        elif guess != answer:
            print("Guess again\n")
game()

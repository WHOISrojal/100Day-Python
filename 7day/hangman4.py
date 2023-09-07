import random

# word_list = ["ardvark","baboon","camel"]
# from hangman_art import stages, logo

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# print(f"The chosen word is {chosen_word}")
end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

print(f'The solution is {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display += "_" 

while not end_of_game:
    guess = input("Enter a letter\n").lower()

if guess in display:
    print("You've already guessed {guess}")

    for position in range(len(chosen_word)): 
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # print(display)
if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life")
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You Lose")

print(f"{' '.join(display)}")

if "_" not in display:  
    end_of_game = True
    print("You Win")

from hangman_art import stages
print(stages[lives])

import random

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)

# print(f"The chosen word is {chosen_word}")

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Enter a letter\n").lower()

for position in range(len(chosen_word)): 
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
    

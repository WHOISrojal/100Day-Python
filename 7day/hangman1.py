# Check whether the letter you entered is in the given word from the list
import random
list = ["ram", "hari","sita"]

chosen_word = random.choice(list)
print(chosen_word)

guess = input("Enter a letter\n").lower()
for letter in chosen_word:
    if letter == guess:
        print("Matched")
    else:
        print("Not Matched")
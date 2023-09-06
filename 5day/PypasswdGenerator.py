print("Welcome to python password generator")
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

no_let = int(input("How many letters do you want to include in the password\t"))
no_num = int(input("How many numbers do you want to include in the password\t"))
no_sym = int(input("How many symbols do you want to include in the password\t"))

password = []
# This line initializes an empty list called password, which will store the characters of the generated password.
for char in range(1, no_let + 1):
    password += random.choice(letters)
# These lines use a loop to add random letters (both uppercase and lowercase) to the password list based on the user's input for the number of letters (no_let).

for char in range(1, no_num + 1):
    password += random.choice(numbers)
    
for char in range(1, no_sym + 1):
    password += random.choice(symbols)

# print(password)
random.shuffle(password)
#This line shuffles the elements in the password list randomly, so the characters are not in the order they were added.
# print(password)

finalpassword = ""
for char in password:
    finalpassword += char
# These lines concatenate the characters in the password list to form the final password string stored in the variable finalpassword.
print(f"Your password is {finalpassword}")
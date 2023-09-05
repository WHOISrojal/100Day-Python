# A simple russian roulette game to determine who will pay for the dinner
import random
name = input("Enter name of person separated by comma who have had dinner\n")
name_sep = name.split(",")
name_len = len(name_sep)

# Generate a random integer between 0 and (name_len - 1)
randoms = random.randint(0, name_len - 1)

# Access the element at the random index to get a random person's name
person = name_sep[randoms]
print(f"{person} will pay the bill")   
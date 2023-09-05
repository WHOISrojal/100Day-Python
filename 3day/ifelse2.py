# Program
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want?")

if size == "s":
    bill = 15
    print("Rs 15")
elif size == "m":
    bill = 20
    print("Rs 20")
else:
    bill = 25
    print("Rs 25")
pep = input("Want pepperoni for pizza?")
if pep == "y":
    if size == "s":
        bill += 2
        print("Rs 2")
    else:
        bill += 3
        print("Rs 3")

cheese = input("Want extra cheese for pizza?")
if cheese == "y":
    bill += 1
    print("Rs 1")
    print("Your bill is",bill)
else:
    print("Your bill is",bill)

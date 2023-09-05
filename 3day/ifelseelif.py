# Program to 
height = int(input("Enter your height:"))

if height > 120:
    print("Can ride")
    age = int(input("Enter your age:"))
    if age < 12:
        print("5 dollar")
        bill = 5
    elif age <= 18:
            print("7 dollar")
            bill = 7
    else:
        print("12 dollar")
        bill = 12
        photo = bool(input("Do you want photos?"))
        if photo == True:
            print("3 dollar")
            bill += 3
            print("Your bill is",bill)
        else:
            print("Your bill is",bill)
else:
    print("Can't ride")



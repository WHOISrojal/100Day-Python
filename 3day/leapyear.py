# Leap year

# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400 

year = int(input("Enter any year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

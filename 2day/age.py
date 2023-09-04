# Create a program using maths and f-strings that tells us how many days, weeks, months we have left if we live until 90 years old

age = int(input("Enter your current age:"))

years = 90 - age
months = years * 12
days = years * 365 
print(f"You have {years} years {months} months and {days} days")

# Write a program that interprets the Body Mass Index (BMI) based on user's weight and height

height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))
bmi = weight/(height**2)
print(bmi)
if bmi > 35:
    print("Clinically obese")
elif bmi > 30 and bmi < 35:
    print("Obese")
elif bmi > 25 and bmi < 30:
    print("Overweight")
elif bmi > 18.5 and bmi < 25:
    print("Normal Weight")
else:
    print("Underweight")
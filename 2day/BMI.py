#(1) Calculate Body Mass Index (BMI) of a person
# Formula       BMI = weight(kg)/height^2(m^2)

height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))
bmi = weight/(height**2)
print(bmi)

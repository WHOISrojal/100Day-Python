# Find out the average height of the students using for loop 

student_height = input("Enter a list of student height").split()
for n in range(0, len(student_height)):
#This line converts each element in the student_height list from a string to an integer using the int() function.
    student_height[n] = int(student_height[n])
# print(student_height)

total_height = 0
for height in student_height:
     total_height += height
print(total_height)

numberofstudent = 0
for student in student_height:
     numberofstudent += 1
    #  print(numberofstudent)

average_height = round(total_height / height)
print(average_height)
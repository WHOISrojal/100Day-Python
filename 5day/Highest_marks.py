# A program to calculate highest score among the scores inputted

student_score = input("Enter a list of student height").split()
for n in range(0, len(student_score)):
#This line converts each element in the student_height list from a string to an integer using the int() function.
    student_score[n] = int(student_score[n])
print(student_score)

highscore = 0
for high in student_score:
    high > highscore
    highscore = high
print(f"The highest marks in class is {highscore}")
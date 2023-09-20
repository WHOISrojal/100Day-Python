from turtle import Turtle, Screen


turt = Turtle()
print(turt) 

turt.shape("arrow")
turt.shape("arrow")
turt.color("blue")

# fd = forward to make turtle move forward
turt.fd(100)

# circle makes the turtle to rotate in a circle
turt.circle(45)

# Screen is a class of a turtle graphics module 
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

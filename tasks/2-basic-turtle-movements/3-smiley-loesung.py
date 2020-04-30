import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")

tina.circle(100)

# left eye
tina.penup()
tina.goto(-50, 100)
tina.pendown()
tina.circle(15)
tina.circle(5)

# right eye
tina.penup()
tina.goto(50, 100)
tina.pendown()
tina.circle(15)
tina.circle(5)

# mouth
tina.penup()
tina.goto(0, 25)
tina.pendown()
tina.circle(30)

window.exitonclick()

import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")

tina.goto(0, 100)
tina.goto(50, 150)
tina.goto(100, 100)
tina.goto(100, 0)
tina.goto(0, 100)
tina.goto(100, 100)
tina.goto(0, 0)
tina.goto(100, 0)

window.exitonclick()

import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")

square_size = 50
square_angle = 90

tina.forward(square_size * 2)
tina.left(square_angle)
tina.forward(square_size)
tina.left(square_angle)
tina.forward(square_size * 2)
tina.left(square_angle)
tina.forward(square_size)

window.exitonclick()

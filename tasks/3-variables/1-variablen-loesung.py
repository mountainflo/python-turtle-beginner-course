import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")

squareSize = 50
squareAngle = 90

tina.forward(squareSize * 2)
tina.left(squareAngle)
tina.forward(squareSize)
tina.left(squareAngle)
tina.forward(squareSize * 2)
tina.left(squareAngle)
tina.forward(squareSize)

window.exitonclick()

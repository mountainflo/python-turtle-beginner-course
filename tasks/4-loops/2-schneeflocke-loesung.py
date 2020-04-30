import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")
tina.speed("fastest")

height = 60

for count in range(6):
    tina.forward(height * 0.6)
    tina.left(60)
    tina.forward(height * 0.4)
    tina.backward(height * 0.4)
    tina.right(120)
    tina.forward(height * 0.4)
    tina.backward(height * 0.4)
    tina.left(60)
    tina.forward(height * 0.4)
    tina.backward(height)
    tina.left(60)

window.exitonclick()

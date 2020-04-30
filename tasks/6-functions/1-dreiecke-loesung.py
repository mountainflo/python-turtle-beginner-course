import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")
tina.speed("fastest")


def triangle(size):
    tina.left(60)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.left(60)


triangle(50)

window.exitonclick()

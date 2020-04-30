import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")
tina.speed("fastest")


def triangle(sizeOfTheTriangle):
    tina.left(60)
    tina.forward(sizeOfTheTriangle)
    tina.left(120)
    tina.forward(sizeOfTheTriangle)
    tina.left(120)
    tina.forward(sizeOfTheTriangle)
    tina.left(60)


def drawSixTriangles(size):
    triangle(size)
    tina.right(60)
    triangle(size)
    tina.right(60)
    triangle(size)
    tina.right(60)
    triangle(size)
    tina.right(60)
    triangle(size)
    tina.right(60)
    triangle(size)


drawSixTriangles(25)
drawSixTriangles(50)
drawSixTriangles(100)
drawSixTriangles(150)

window.exitonclick()

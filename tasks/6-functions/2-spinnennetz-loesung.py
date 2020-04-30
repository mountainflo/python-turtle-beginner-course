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


def draw_six_triangles(size):
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


draw_six_triangles(25)
draw_six_triangles(50)
draw_six_triangles(100)
draw_six_triangles(150)

window.exitonclick()

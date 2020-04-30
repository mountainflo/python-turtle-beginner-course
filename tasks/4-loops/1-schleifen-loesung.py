import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")

tina.speed("fastest")

for count in range(100):
    tina.color("green")
    tina.forward(count * 2)
    tina.left(60)

window.exitonclick()

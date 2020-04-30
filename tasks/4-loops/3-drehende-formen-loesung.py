import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")
tina.speed("fastest")

# rotating circles
for i in range(73):
    tina.circle(80)
    tina.right(10)

# rotating and growing squares
"""
for i in range(73):
    width = 10 + 2 * i
    for count in range(4):
        tina.forward(width)
        tina.left(90)
    tina.right(10)
"""

window.exitonclick()

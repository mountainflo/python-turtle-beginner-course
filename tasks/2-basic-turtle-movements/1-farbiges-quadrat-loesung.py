import turtle

# for detailed documentation of "Turtle graphics" library see:
# https://docs.python.org/3/library/turtle.html

window = turtle.Screen()

tina = turtle.Turtle()

# black, red, green, yellow, pink ... (for more colors see: https://trinket.io/docs/colors)
tina.color("blue")
tina.shape("turtle")  # "arrow", "turtle", "circle", "square", "classic"

tina.forward(100)
tina.left(90)
tina.color("magenta")
tina.forward(100)
tina.left(90)
tina.color("red")
tina.forward(100)
tina.left(90)
tina.color("green")
tina.forward(100)
tina.left(90)

window.exitonclick()

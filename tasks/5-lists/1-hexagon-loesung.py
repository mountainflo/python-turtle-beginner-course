import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")
tina.speed("fastest")

# colored hexagon
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for i in range(len(colors)):
    tina.color(colors[i])
    tina.forward(100)
    tina.left(60)


# Rainbow Benzene
# from https://www.geeksforgeeks.org/turtle-programming-python/
"""
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

tina.speed("fastest")

for x in range(200):
    tina.pencolor(colors[x % 6])
    tina.width(int(x / 100) + 1)
    tina.forward(x)
    tina.left(59)
"""

window.exitonclick()

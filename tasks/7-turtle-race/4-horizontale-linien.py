import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("purple")
tina.shape("turtle")
tina.speed("fastest")


##################################
# Aufgabe 1: Skala am oberen Spielfeldrand


def drawScala(size):
    for step in range(size):
        tina.write(step, align="center")
        tina.forward(20)


tina.penup()
tina.goto(-200, 200)
tina.pendown()

sizeOfTheRaceTrack = 21
drawScala(sizeOfTheRaceTrack)

tina.penup()
tina.goto(0, 0)
tina.pendown()


##################################
# Aufgabe 4: Horizontale Linien

def drawHorizontalLines(count, size):
    for step in range(count):
        tina.right(90)
        tina.forward(size)
        tina.penup()
        tina.backward(size)
        tina.left(90)
        tina.forward(20)
        tina.pendown()

    tina.penup()
    tina.backward(size * 20)
    tina.pendown()


tina.penup()
tina.goto(-200, 190)
tina.pendown()

drawHorizontalLines(sizeOfTheRaceTrack, 190)

tina.penup()
tina.goto(0, 0)
tina.pendown()

##################################
# Aufgabe 2: Mehrere Schildkroeten

ada = turtle.Turtle()
ada.shape("turtle")
ada.color("blue")
ada.penup()
ada.goto(-200, 160)
ada.pendown()

hans = turtle.Turtle()
hans.shape("turtle")
hans.color("green")
hans.penup()
hans.goto(-200, 100)
hans.pendown()

fritz = turtle.Turtle()
fritz.shape("turtle")
fritz.color("black")
fritz.penup()
fritz.goto(-200, 40)
fritz.pendown()

##################################
# Aufgabe 3: Zufallswerte

from random import randint

for move in range(150):
    ada.forward(randint(1, 5))
    hans.forward(randint(1, 5))
    fritz.forward(randint(1, 5))

window.exitonclick()

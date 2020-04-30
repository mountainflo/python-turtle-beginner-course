from random import randint
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
# Erweiterung: Karierte Ziellinie

def drawFinishLine(height):
    for i in range(int(height / 10)):
        if i % 2 == 0:
            tina.begin_fill()

        for j in range(4):
            tina.forward(10)
            tina.right(90)

        if i % 2 == 0:
            tina.end_fill()

        tina.right(90)
        tina.forward(10)
        tina.left(90)


tina.penup()
tina.goto(200, 190)
tina.pendown()

drawFinishLine(190)

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
# Aufgabe 5: Gewinner Schildkroete

turtleNames = ["Ada", "Hans", "Fritz"]


def startRace():
    finishLineXCor = 190

    for move in range(200):
        ada.forward(randint(1, 5))
        if (ada.xcor() > finishLineXCor):
            return 0

        hans.forward(randint(1, 5))
        if (hans.xcor() > finishLineXCor):
            return 1

        fritz.forward(randint(1, 5))
        if (fritz.xcor() > finishLineXCor):
            return 2


print("Welche Schildkröte gewinnt: blau Ada(0), grün Hans(1), schwarz Fritz(2)?")
betPlayer1 = int(input("Wette von Spieler 1:"))
betPlayer2 = int(input("Wette von Spieler 2:"))

winnerTurtle = startRace()
print("Schildkröte " + turtleNames[winnerTurtle] + " hat gewonnen!")

if betPlayer2 == betPlayer1 and winnerTurtle == betPlayer2:
    print("Beide Spieler haben gewonnen!")
elif winnerTurtle == betPlayer1:
    print("Spieler 1 hat das Spiel gewonnen!")
elif winnerTurtle == betPlayer2:
    print("Spieler 2 hat das Spiel gewonnen!")
else:
    print("Keine der Wetten war richtig. Beide Spieler haben verloren.")

window.exitonclick()

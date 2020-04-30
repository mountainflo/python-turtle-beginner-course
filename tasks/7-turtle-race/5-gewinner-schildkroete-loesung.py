from random import randint
import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("purple")
tina.shape("turtle")
tina.speed("fastest")


##################################
# Aufgabe 1: Skala am oberen Spielfeldrand


def draw_scala(size):
    for step in range(size):
        tina.write(step, align="center")
        tina.forward(20)


tina.penup()
tina.goto(-200, 200)
tina.pendown()

race_track_size = 21
draw_scala(race_track_size)

tina.penup()
tina.goto(0, 0)
tina.pendown()


##################################
# Aufgabe 4: Horizontale Linien

def draw_horizontal_lines(count, size):
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

draw_horizontal_lines(race_track_size, 190)

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


def start_race():
    finish_line_x_cor = 200

    for move in range(200):
        ada.forward(randint(1, 5))
        if ada.xcor() >= finish_line_x_cor:
            print("Ada wins!")
            return

        hans.forward(randint(1, 5))
        if hans.xcor() >= finish_line_x_cor:
            print("Hans wins!")
            return

        fritz.forward(randint(1, 5))
        if fritz.xcor() >= finish_line_x_cor:
            print("Fritz wins!")
            return


start_race()

window.exitonclick()

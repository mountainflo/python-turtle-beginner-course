import turtle

window = turtle.Screen()
tina = turtle.Turtle()

tina.color("blue")
tina.shape("turtle")
tina.speed("fastest")


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

window.exitonclick()

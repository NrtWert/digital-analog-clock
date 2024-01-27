import turtle
from datetime import datetime

wn = turtle.Screen()
wn.title("digital-analog clock")
wn.bgcolor('#FFD460')
wn.setup(width=500, height=500)
wn.tracer(0)

clr = '#2D4059'

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):
    pen.up()
    pen.goto(0, -210)
    pen.setheading(0)
    pen.color(clr)
    pen.pendown()
    pen.circle(210)

    for x in range(12):
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(-30 * (x + 1))
        pen.forward(188)
        pen.pendown()
        pen.forward(20)

    pen.penup()
    pen.goto(0, 0)
    pen.color(clr)
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.forward(19)
    pen.pendown()
    for i in range(5):
        pen.write(datetime.now().hour, align="center", font=("Comic Sans MS", 10, "bold"))
        pen.penup()
        pen.forward(19)
        pen.pendown()

    pen.penup()
    pen.goto(0, 0)
    pen.color(clr)
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.forward(19)
    pen.pendown()
    for i in range(7):
        pen.write(datetime.now().minute, align="center", font=("Comic Sans MS", 10, "bold"))
        pen.penup()
        pen.forward(19)
        pen.pendown()

    pen.penup()
    pen.goto(0, 0)
    pen.color(clr)
    pen.setheading(90)
    angle = (s / 600) * 360
    pen.rt(angle)
    pen.pendown()
    for i in range(10):
        pen.write(datetime.now().second, align="center", font=("Comic Sans MS", 10, "bold"))
        pen.penup()
        pen.forward(19)
        pen.pendown()

try:
    while True:
        if wn.window_height() != 1017 or wn.window_width() != 1920:
            if wn.window_height() != 500 or wn.window_width() != 500:
                wn.setup(width=500, height=500)

        h = int(datetime.now().hour)
        m = int(datetime.now().minute)
        s = int(datetime.now().microsecond // 100000 + datetime.now().second * 10)

        draw_clock(h, m, s, pen)

        wn.update()
        pen.clear()
except:
    pass
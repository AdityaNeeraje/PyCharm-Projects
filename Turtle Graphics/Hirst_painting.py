from turtle import *
from tkinter import TclError
from random import randint


def draw_circle(turtle):
    turtle.forward(forward_distance)
    turtle.pendown()
    turtle.dot(radius, (randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.penup()


radius = 10
forward_distance = 20
canvwidth = 470
canvheight = 400
try:
    screen = Screen()
    screen.colormode(255)
    screen.bgcolor("cyan2")
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(x=-canvwidth, y=-canvheight+5)
    turtle.setheading(0)
    while True:
        if abs(turtle.ycor()) > (canvheight+10):
            break
        if abs(turtle.xcor()) > canvwidth:
            if turtle.heading() == 0:
                for n in range(2):
                    turtle.left(90)
                    draw_circle(turtle)
            elif turtle.heading() == 180:
                for n in range(2):
                    turtle.right(90)
                    draw_circle(turtle)
        draw_circle(turtle)

    screen.mainloop()
except (KeyboardInterrupt, TclError, Terminator):
    pass

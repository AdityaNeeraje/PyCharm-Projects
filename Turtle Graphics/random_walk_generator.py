# Note: The window can be closed by pressing Enter at any point during the random walk.

from turtle import *
from tkinter import TclError
from math import sin, cos, pi
from time import sleep
from random import choice, randint
import threading


def event_one():
    global should_continue, turtle, screen
    while should_continue:
        random_direction = choice(
            [heading for heading in [0, 90, 180, 270] if heading != (int(turtle.heading()) + 180) % 360])
        turtle.setheading(random_direction)
        turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        if abs(turtle.xcor() + forward_distance * cos(random_direction * pi / 180)) <= canvwidth and abs(
                turtle.ycor() + forward_distance * sin(random_direction * pi / 180)) <= canvheight:
            turtle.forward(forward_distance)
        screen.listen()

        def exit_loop():
            global should_continue
            screen.bye()
            should_continue = False

        screen.onkeypress(exit_loop, "Return")
        screen.onkeypress(exit_loop, "Escape")

def event_two():
    global should_continue
    sleep(300)
    should_continue = False

pensize = 20
forward_distance = 30
canvwidth = 470
canvheight = 400

screen = Screen()
screen.bgcolor("azure2")
screen.colormode(255)
turtle = Turtle()
turtle.pensize(pensize)
turtle.hideturtle()
try:
    should_continue = True
    thread1 = threading.Thread(target=event_one)
    thread2 = threading.Thread(target=event_two)
    thread1.start()
    thread2.start()
    screen.mainloop()
    thread1.join()
    thread2.join()
    sleep(10)
except (KeyboardInterrupt, TclError, Terminator):
    pass

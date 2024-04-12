import turtle
from turtle import *
from math import pi, sin, cos
from time import sleep

from math import pi, sin, cos, atan, tan
from turtle import *

screen = Screen()

# exponent_turtle = Turtle()
# exponent_turtle.hideturtle()
# exponent_turtle.penup()
# exponent_turtle.goto(0, 1)
# exponent_turtle.pendown()
# for n in range(10):
#     exponent_turtle.goto(exponent_turtle.pos()[0] + 0.5, 2.71828**(exponent_turtle.pos()[0] + 0.5))
#     print(exponent_turtle.pos())

other_turtle = Turtle()
other_turtle.color("red")
other_turtle.hideturtle()
other_turtle.penup()
other_turtle.goto(0, 1)
other_turtle.pendown()
direction = 45
other_turtle.setheading(direction)
slope = 1
forward_distance = 0.1
for n in range(100):
    original_direction = direction
    other_turtle.forward(forward_distance)
    slope += forward_distance*sin(pi/180*direction)
    print(slope/(2.71828**other_turtle.pos()[0]))
    direction = 180/pi*atan(slope)
    other_turtle.left(direction - original_direction)
    # print(other_turtle.pos())

screen.mainloop()
# from turtle import *
# from tkinter import TclError
# from time import sleep
# from math import sin, cos, pi
# import json
#
# image_turtle_x = 350
# image_turtle_y = 290
# hexagon_vertices = ((5.5, 9), (9.5, 0), (5.5, -9), (-5.5, -9), (-9.5, 0), (-5.5, 9))
#
# with open("colors_and_coordinates.json", "r") as file:
#     colors_and_coordinates_dict = json.load(file)
#
# try:
#     def change_color(clicked_turtle, x, y):
#         global etching_turtle
#         red = int(clicked_turtle.color()[0][0])
#         green = int(clicked_turtle.color()[0][1])
#         blue = int(clicked_turtle.color()[0][2])
#         etching_turtle.color(red, green, blue)
#         screen.bgcolor(255 - red, 255 - green, 255 - blue)
#
#
#     screen = Screen()
#     screen.tracer(0)
#     screen.register_shape("img.gif")
#     image_turtle = Turtle("img.gif")
#     image_turtle.penup()
#     image_turtle.goto(image_turtle_x, image_turtle_y)
#     screen.register_shape("hexagon", shape=hexagon_vertices)
#     for key, value in colors_and_coordinates_dict.items():
#         hexagon_turtle = Turtle("hexagon")
#         hexagon_turtle.speed("fastest")
#         hexagon_turtle.penup()
#         hexagon_turtle.goto(value[0], value[1])
#         hexagon_turtle.color(key)
#         hexagon_turtle.onclick(lambda x, y, turtle=hexagon_turtle: change_color(turtle, x, y))
#     screen.update()
#
#     turtle_heading = 0
#     turtle_baseheading = 0
#     should_pause = False
#
#
#     def rebound():
#         global turtle_baseheading
#         try:
#             etching_turtle.penup()
#             etching_turtle.forward(5)
#             etching_turtle.right(180)
#             etching_turtle.forward(5)
#             turtle_baseheading += 180
#             etching_turtle.pendown()
#         except (TclError, KeyboardInterrupt, Terminator):
#             pass
#
#
#     def move_in_direction(angle):
#         global turtle_heading, should_pause, turtle_baseheading
#         angle -= 90 * int(((turtle_baseheading + 45) % 360) / 90)
#         try:
#             should_pause = False
#             turtle_heading = turtle_baseheading + angle
#             if etching_turtle.heading() != turtle_heading:
#                 etching_turtle.setheading(turtle_heading)
#             while not abs(
#                     etching_turtle.xcor() + 10 * cos(pi / 180 * etching_turtle.heading())) > width and not abs(
#                 etching_turtle.ycor() + 10 * sin(
#                     pi / 180 * etching_turtle.heading())) > height and not should_pause:
#                 etching_turtle.forward(10)
#                 screen.update()
#                 sleep(0.1)
#                 # if 350 < turtle.xcor() < 440 and 270 < turtle.ycor() < 420:
#                 #     red.lower()
#                 #     green.lower()
#                 #     blue.lower()
#                 # else:
#                 #     red.lift()
#                 #     green.lift()
#                 #     blue.lift()
#             if abs(etching_turtle.xcor() + 10 * cos(pi / 180 * turtle_heading)) > width or abs(
#                     etching_turtle.ycor() + 10 * sin(pi / 180 * turtle_heading)) > height:
#                 rebound()
#             screen.update()
#         except (TclError, KeyboardInterrupt, Terminator):
#             pass
#
#
#     def pause_turtle(should_clear=False):
#         try:
#             global should_pause
#             should_pause = True
#             if should_clear:
#                 etching_turtle.clear()
#         except (TclError, KeyboardInterrupt, Terminator):
#             pass
#
#
#     def turn_right():
#         global turtle_baseheading
#         etching_turtle.right(10)
#         turtle_baseheading -= 10
#         sleep(0.1)
#         screen.update()
#
#
#     def turn_left():
#         global turtle_baseheading
#         etching_turtle.left(10)
#         turtle_baseheading += 10
#         sleep(0.1)
#         screen.update()
#
#
#     # def on_slider_change(value):
#     #     try:
#     #         turtle.color((red.get(), green.get(), blue.get()))
#     #         screen.bgcolor((255-red.get(), 255-green.get(), 255-blue.get()))
#     #         red.config(bg='#{:02x}{:02x}{:02x}'.format(255 - red.get(), 255 - green.get(), 255 - blue.get()))
#     #         blue.config(bg='#{:02x}{:02x}{:02x}'.format(255 - red.get(), 255 - green.get(), 255 - blue.get()))
#     #         green.config(bg='#{:02x}{:02x}{:02x}'.format(255 - red.get(), 255 - green.get(), 255 - blue.get()))
#     #     except (TclError, KeyboardInterrupt, Terminator):
#     #         pass
#
#     screen.listen()
#     screen.register_shape("img.gif")
#     image_turtle = Turtle("img.gif")
#     image_turtle.penup()
#     image_turtle.goto(350, 290)
#     width, height = screen.window_width() / 2 - 10, screen.window_height() / 2 - 10
#     etching_turtle = Turtle()
#     etching_turtle.shape("triangle")
#     etching_turtle.pensize(5)
#     etching_turtle.speed('slowest')
#     # red = Scale(from_=0, to=255, orient=HORIZONTAL, bg="white", fg="red", troughcolor="red", highlightthickness=0, command=on_slider_change)
#     # blue = Scale(from_=0, to=255, orient=HORIZONTAL, bg="white", fg="blue", troughcolor="blue", highlightthickness=0, command=on_slider_change)
#     # green = Scale(from_=0, to=255, orient=HORIZONTAL, bg="white", fg="green", troughcolor="chartreuse3", highlightthickness=0, command=on_slider_change)
#     # red.place(x=830, y=10)
#     # green.place(x=830, y=50)
#     # blue.place(x=830, y=90)
#
#     screen.update()
#     screen.onkey(lambda: move_in_direction(90), "Up")
#     screen.onkey(lambda: move_in_direction(270), "Down")
#     screen.onkey(lambda: move_in_direction(0), "Right")
#     screen.onkey(lambda: move_in_direction(180), "Left")
#     screen.onkey(lambda: move_in_direction(90), "w")
#     screen.onkey(lambda: move_in_direction(270), "s")
#     screen.onkey(turn_right, "d")
#     screen.onkey(turn_left, "a")
#     screen.onkey(pause_turtle, "space")
#     screen.onkey(lambda: pause_turtle(should_clear=True), "Return")
#     screen.colormode(255)
#     screen.mainloop()
# except (TclError, KeyboardInterrupt, Terminator, TypeError) as error:
#     pass
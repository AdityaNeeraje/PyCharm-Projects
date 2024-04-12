import turtle
from time import time, sleep
from turtle import Turtle, ontimer
from random import randint
import threading


class Food(Turtle):
    def __init__(self, screen, snake_segments):
        super().__init__()
        self.explode_turtles = []
        self.snake_segments = snake_segments
        self.shape("circle")
        self.shapesize(0.4, 0.4)
        self.color("NavyBlue")
        self.penup()
        self.move_to_new_position(screen)

    def move_to_new_position(self, screen):
        random_point = [randint(-int(screen.window_width() / 2) + 15, int(screen.window_width() / 2) - 15),
                        randint(-int(screen.window_height() / 2) + 15, int(screen.window_height() / 2) - 15)]
        self.setpos(random_point[0], random_point[1])
        explode_turtle = Turtle()
        explode_turtle.hideturtle()
        explode_turtle.color("red")
        explode_turtle.penup()
        explode_turtle.setpos(random_point[0], random_point[1])
        self.explode_turtles.append(explode_turtle)
        self.screen.update()

    def explode(self):
        try:
            exploding_turtle = self.explode_turtles[-1]
            self.move_to_new_position(self.screen)
            exploding_turtle.pendown()
            for i in range(50):
                angle = randint(0, 45)
                distance = randint(0, 20)
                exploding_turtle.right(angle)
                exploding_turtle.forward(distance)
                exploding_turtle.backward(distance)
            self.screen.update()
            ontimer(lambda: self.fade_out(exploding_turtle), 10000)
            exploding_turtle.penup()
        except IndexError as error:
            print(error)

    def fade_out(self, exploding_turtle, intensity=0.9):
        exploding_turtle.clear()
        try:
            self.explode_turtles.remove(exploding_turtle)
        except ValueError:
            pass
        # self.draw_explosion(exploding_turtle)
        # intensity -= 0.1
        # if intensity > 0.1:
        #     ontimer(lambda: self.fade_out(exploding_turtle, intensity), 2000)
        # else:
        #     exploding_turtle.clear()
        #     self.explode_turtles.remove(exploding_turtle)

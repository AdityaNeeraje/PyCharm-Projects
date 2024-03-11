from turtle import Turtle, Terminator
from tkinter import TclError
from time import sleep
from scoreboard import ScoreBoard
from math import cos, sin, pi
from food import Food
from random import randint

dictionary_of_speeds = {"easy": 0.125, "medium": 0.1, "hard": 0.06, "extra hard": 0.04}
change_color = True
continue_playing = True

class Snake:
    def __init__(self, screen):
        # Set initial variables
        self.game_over = False
        self.game_paused = False
        self.snake_segments = []
        self.screen = screen
        self.canvwidth, self.canvheight = self.screen.window_width(), self.screen.window_height()

        # Prompt user for difficulty level and initialize the ScoreBoard class, which relies on the difficulty level
        self.speed = self.screen.textinput("Welcome to the Snake Game",
                                           "Choose your difficulty level: Easy/Medium/Hard/Extra Hard")
        while True:
            if isinstance(self.speed, str):
                if ['easy', 'medium', 'hard', 'extra hard'].count(self.speed.strip().lower()) != 0:
                    self.speed = self.speed.strip().lower()
                    break
            self.speed = self.screen.textinput("Welcome to the Snake Game",
                                               "Please choose one of Easy/Medium/Hard/Extra Hard:")
        self.scoreboard = ScoreBoard(screen, self.speed)

        # Create the snake and get it to start moving
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        for n in range(5):
            snake_segment = Turtle()
            snake_segment.penup()
            snake_segment.shape("square")
            snake_segment.color("white")
            if change_color:
                snake_segment.color(random_color)
            snake_segment.goto(-n * 5, 0)
            snake_segment.speed("fastest")
            self.snake_segments.append(snake_segment)
        self.leading_segment = self.snake_segments[0]
        self.food_particle = Food(self.screen, self.snake_segments)
        # self.leading_segment.setheading(90)
        # self.move_in_direction(0)

    def move_in_direction(self, angle):
        try:
            if (self.leading_segment.heading() - angle) % 180 != 0 or self.leading_segment.heading() == angle:
                self.leading_segment.setheading(angle)
                while not self.game_over and not self.game_paused:
                    self.snake_segments[0].forward(10)
                    for n in range(len(self.snake_segments))[::-1][:-1]:
                        self.snake_segments[n].goto(self.snake_segments[n - 1].pos())
                    self.check_if_game_over()
                    self.check_if_food_eaten()
                    self.screen.update()
                    self.screen.listen()
                    self.screen.onkeypress(lambda: self.move_in_direction(90), "Up")
                    self.screen.onkeypress(lambda: self.move_in_direction(270), "Down")
                    self.screen.onkeypress(lambda: self.move_in_direction(0), "Right")
                    self.screen.onkeypress(lambda: self.move_in_direction(180), "Left")
                    self.screen.onkeypress(lambda: self.move_in_direction(90), "w")
                    self.screen.onkeypress(lambda: self.move_in_direction(270), "s")
                    self.screen.onkeypress(lambda: self.move_in_direction(0), "d")
                    self.screen.onkeypress(lambda: self.move_in_direction(180), "a")
                    self.screen.onkeypress(self.pause_game, "space")
                    self.screen.onkeypress(self.pause_game, "Return")
                    sleep(dictionary_of_speeds[self.speed])
        except RecursionError as error:
            sleep(1)
            print(error)

    def pause_game(self):
        self.game_paused = not self.game_paused
        self.move_in_direction(self.leading_segment.heading())

    def check_if_game_over(self):
        if abs(self.leading_segment.xcor()) > self.canvwidth / 2 - 5 or abs(
                self.leading_segment.ycor()) > self.canvheight / 2 - 5 or any(
            abs(self.leading_segment.xcor() - segment.xcor()) < 5 and abs(
                self.leading_segment.ycor() - segment.ycor()) < 5 for segment in self.snake_segments[2:]):
            self.game_over = True
            self.ask_to_continue_turtle = Turtle()
            self.ask_to_continue_turtle.penup()
            self.ask_to_continue_turtle.goto(0, self.canvheight*0.4)
            self.ask_to_continue_turtle.color("red")
            self.ask_to_continue_turtle.hideturtle()
            self.ask_to_continue_turtle.write("GAME OVER!", align="center", font=("Arial", 18, "bold"))
            self.ask_to_continue_turtle.goto(0, self.canvheight*0.4 - 50)
            self.ask_to_continue_turtle.write("Press Enter to Play Again, Esc to Exit", align="center", font=("Arial", 18, "bold"))
            self.screen.update()

    def check_if_food_eaten(self):
        if abs(self.leading_segment.xcor() - self.food_particle.xcor()) <= 12 and abs(
                self.leading_segment.ycor() - self.food_particle.ycor()) <= 12 and not self.game_paused and not self.game_over:
            self.scoreboard.score += 1
            self.scoreboard.display_score()
            snake_segment = Turtle()
            snake_segment.color("white")
            snake_segment.shape("square")
            snake_segment.penup()
            snake_segment.speed("fastest")
            snake_segment.goto(self.snake_segments[-1].xcor() - 10 * cos(pi / 180 * self.snake_segments[-1].heading()),
                               self.snake_segments[-1].ycor() - 10 * sin(pi / 180 * self.snake_segments[-1].heading()))
            self.snake_segments.append(snake_segment)
            random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            if change_color:
                for snake_segment in self.snake_segments:
                    snake_segment.color(random_color)
            self.food_particle.snake_segments = self.snake_segments
            self.food_particle.explode()
            self.screen.update()

    def destroy_game(self):
        try:
            self.screen.bye()
        except (TclError, Terminator, KeyboardInterrupt):
            pass

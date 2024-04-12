import json
from turtle import Turtle

with open("high_scores.csv", "r") as file:
    high_score_data = json.load(file)

class ScoreBoard:
    def __init__(self, screen, difficulty_level):
        self.score = 0
        self.difficulty_level = difficulty_level
        self.score_turtle = Turtle()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.color("white")
        self.score_turtle.goto(-screen.window_width()/2*0.6, screen.window_height()/2-50)
        self.score_turtle.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))
        self.highscore = high_score_data.get(difficulty_level)
        self.highscore_turtle = Turtle()
        self.highscore_turtle.penup()
        self.highscore_turtle.hideturtle()
        self.highscore_turtle.color("white")
        self.highscore_turtle.goto(screen.window_width()/2*0.6, screen.window_height()/2-50)
        self.highscore_turtle.write(f"High Score: {self.highscore}", align="center", font=("Arial", 16, "bold"))

    def display_score(self):
        self.score_turtle.clear()
        self.score_turtle.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))
        print(f"Score: {self.score}")
        if self.score > self.highscore:
            self.highscore = self.score
            high_score_data[self.difficulty_level] = self.highscore
            with open("high_scores.csv", "w") as file:
                json.dump(high_score_data, file, indent=4)
            self.highscore_turtle.clear()
            self.highscore_turtle.write(f"High Score: {self.highscore}", align="center", font=("Arial", 16, "bold"))
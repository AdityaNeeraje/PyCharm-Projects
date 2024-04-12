# Press space or return to pause the game

from turtle import *
from snake import Snake, dictionary_of_speeds, continue_playing
from time import sleep


def restart_game():
    screen.clear()
    start_game()


def start_game():
    screen.colormode(255)
    screen.bgcolor("black")
    screen.listen()
    screen.tracer(0)

    def move_in_direction(angle):
        try:
            if ((
                        snake.leading_segment.heading() - angle) % 180 != 0 or snake.leading_segment.heading() == angle) and not snake.game_paused and not snake.game_over:
                snake.leading_segment.setheading(angle)
                while not snake.game_over and not snake.game_paused:
                    snake.leading_segment.forward(10)
                    for n in range(len(snake.snake_segments))[::-1][:-1]:
                        snake.snake_segments[n].goto(snake.snake_segments[n - 1].pos())
                    snake.check_if_game_over()
                    snake.check_if_food_eaten()
                    screen.update()
                    sleep(dictionary_of_speeds[snake.speed])
        except RecursionError as error:
            sleep(1)
            print(error)

    def pause_game():
        snake.game_paused = not snake.game_paused
        move_in_direction(snake.leading_segment.heading())

    snake = Snake(screen)
    snake.move_in_direction(0)
    screen.listen()
    screen.onkeypress(lambda: move_in_direction(90), "Up")
    screen.onkeypress(lambda: move_in_direction(270), "Down")
    screen.onkeypress(lambda: move_in_direction(0), "Right")
    screen.onkeypress(lambda: move_in_direction(180), "Left")
    screen.onkeypress(lambda: move_in_direction(90), "w")
    screen.onkeypress(lambda: move_in_direction(270), "s")
    screen.onkeypress(lambda: move_in_direction(0), "d")
    screen.onkeypress(lambda: move_in_direction(180), "a")
    screen.onkeypress(pause_game, "space")
    screen.onkeypress(snake.destroy_game, "Escape")
    screen.onkeypress(restart_game, "Return")


screen = Screen()
start_game()
screen.mainloop()

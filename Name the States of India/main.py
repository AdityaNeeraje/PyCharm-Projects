from turtle import *
from tkinter import TclError
import pandas
from time import sleep
from random import *


def start_game():
    try:
        global turtle_list, score, guessed_states
        for turtle in turtle_list:
            turtle.clear()
        score_turtle.clear()
        score = 0
        guessed_states = []
        user_input = screen.textinput(title=f"{score}/{len(states_list)} States guessed", prompt="Guess another state:")
        while True:
            hint_turtle.clear()
            if isinstance(user_input, str) and user_input.strip().title() in states_list and user_input.strip().title() not in guessed_states:
                score += 1
                guessed_states.append(user_input.strip().title())
                turtle_list[states_list.index(user_input.strip().title())].write(user_input.strip().title(),
                                                                                 align="center",
                                                                                 font=("Arial", 9, "bold"))
                screen.update()
                if score == len(states_list):
                    score_turtle.goto(0, 0)
                    score_turtle.write(f"Congratulations! You have Named all {len(states_list)} States", align="center",
                                       font=("Arial", 18, "bold"))
                    score_turtle.goto(x=0, y=-40)
                    score_turtle.write(f"Press Enter to Play again, Esc to Exit", align="center",
                                       font=("Arial", 18, "bold"))
                    break
                else:
                    user_input = screen.textinput(title=f"{score}/{len(states_list)} States guessed",
                                                  prompt="Guess another state:")
            elif isinstance(user_input, str) and user_input.strip().title() in guessed_states:
                user_input = screen.textinput(title=f"{score}/{len(states_list)} States guessed",
                                                  prompt="You have already guessed that state. Name another state:")
            elif isinstance(user_input, str) and user_input.strip().lower() == "give up":
                for n in [states_list.index(state) for state in states_list if state not in guessed_states]:
                    turtle_list[n].color("red")
                    turtle_list[n].write(states_list[n], align="center", font=("Arial", 9, "bold"))
                    turtle_list[n].color("black")
                    screen.update()
                    sleep(0.1)
                score_turtle.goto(0, 0)
                score_turtle.write(f"You have Named {score}/{len(states_list)} States", align="center",
                                   font=("Arial", 18, "bold"))
                score_turtle.goto(x=0, y=-40)
                score_turtle.write(f"Press Enter to Play again, Esc to Exit", align="center",
                                   font=("Arial", 18, "bold"))
                break
            elif isinstance(user_input, str) and user_input.strip().lower() == "hint":
                give_hint()
                user_input = screen.textinput(title=f"{score}/{len(states_list)} States guessed",
                                              prompt="Guess another state:")
            elif user_input is None:
                user_input = screen.textinput(title=f"{score}/{len(states_list)} States guessed",
                                              prompt="Guess another state:")
            elif isinstance(user_input, str) and not user_input.strip().title() in states_list:
                user_input = screen.textinput(title=f"{score}/{len(states_list)} States guessed",
                                              prompt="Please enter a valid state name:")
        sleep(2)

        screen.listen()
        screen.onkey(fun=start_game, key="Return")
        screen.onkey(fun=destroy_game, key="Escape")
    except (TclError, KeyboardInterrupt, Terminator):
        pass


def give_hint():
    chosen_state = choice([state for state in states_list if state not in guessed_states])
    random_indices = choices([index for index in range(len(chosen_state)) if chosen_state[index] != " "], k=round(len(chosen_state) / 3))
    string = ''.join([chosen_state[index] if index in random_indices or chosen_state[index] == " " else "*" for index in range(len(chosen_state))])
    hint_turtle.write(f"Here's a hint: {string}", align="center", font=("Arial", 22, "bold"))


def destroy_game():
    try:
        screen.bye()
    except (TclError, Terminator, KeyboardInterrupt):
        pass


data = pandas.read_csv("states_of_india.csv")
states_list = data['state'].tolist()

screen = Screen()
screen.title("Name the States of India")
screen.setup(width=709, height=811)
screen.bgpic("india_states_map.png")
screen.tracer(0)

turtle_list = []
for state in states_list:
    state_turtle = Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x=data[data['state'] == state]['x'].iloc[0], y=data[data['state'] == state]['y'].iloc[0])
    turtle_list.append(state_turtle)
screen.update()

score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.penup()

hint_turtle = Turtle()
hint_turtle.hideturtle()
hint_turtle.penup()
hint_turtle.color("orange")

guessed_states = []
score = 0
start_game()

screen.mainloop()
from turtle import *
import pandas

data = pandas.read_csv("states_of_india.csv")
states_list = data['state'].tolist()


def choose_new_state():
    with open("states_of_india.csv", "w") as file:
        data.to_csv(file, sep=",", index=False, encoding="utf-8")
    global n
    state = screen.textinput(title="Setting State Coordinates", prompt="Enter a new state name:")
    try:
        n = states_list.index(state.strip().title())
        for turtle in turtle_list:
            if turtle.color() != ("black", "black"):
                turtle.color("black")
                turtle.clear()
                turtle.write(states_list[turtle_list.index(turtle)], align="center", font=("Arial", 8, 'bold'))
        turtle_list[n].color("red")
        turtle_list[n].clear()
        turtle_list[n].write(states_list[n], align="center", font=("Arial", 8, 'bold'))
    except:
        pass
    screen.listen()
    screen.onkey(lambda: move_in_direction(90, turtle_list[n]), "Up")
    screen.onkey(lambda: move_in_direction(270, turtle_list[n]), "Down")
    screen.onkey(lambda: move_in_direction(0, turtle_list[n]), "Right")
    screen.onkey(lambda: move_in_direction(180, turtle_list[n]), "Left")
    screen.onkey(lambda: small_move_in_direction(90, turtle_list[n]), "w")
    screen.onkey(lambda: small_move_in_direction(270, turtle_list[n]), "s")
    screen.onkey(lambda: small_move_in_direction(0, turtle_list[n]), "d")
    screen.onkey(lambda: small_move_in_direction(180, turtle_list[n]), "a")
    screen.onkey(choose_new_state, "Tab")


def move_in_direction(angle, moving_turtle):
    moving_turtle.clear()
    moving_turtle.setheading(angle)
    moving_turtle.forward(10)
    moving_turtle.write(states_list[n], align="center", font=("Arial", 8, "bold"))
    data.loc[data['state'] == states_list[turtle_list.index(moving_turtle)], 'x'] = moving_turtle.pos()[0]
    data.loc[data['state'] == states_list[turtle_list.index(moving_turtle)], 'y'] = moving_turtle.pos()[1]
    screen.update()



def small_move_in_direction(angle, moving_turtle):
    moving_turtle.clear()
    moving_turtle.setheading(angle)
    moving_turtle.forward(1)
    moving_turtle.write(states_list[n], align="center", font=("Arial", 8, "bold"))
    data.loc[data['state'] == states_list[turtle_list.index(moving_turtle)], 'x'] = moving_turtle.pos()[0]
    data.loc[data['state'] == states_list[turtle_list.index(moving_turtle)], 'y'] = moving_turtle.pos()[1]
    screen.update()


screen = Screen()
screen.title("Name the States of India")
screen.setup(width=711, height=811)
screen.bgpic("india_states_map.png")
screen.tracer(0)

turtle_list = []
for state in states_list:
    state_turtle = Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x=data[data['state'] == state]['x'].iloc[0], y=data[data['state'] == state]['y'].iloc[0])
    state_turtle.write(state, align="center", font=("Arial", 8, "bold"))
    turtle_list.append(state_turtle)
screen.update()

n = 0
choose_new_state()

screen.mainloop()

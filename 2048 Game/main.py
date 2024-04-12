from tkinter import Tk, Label, StringVar, Canvas, Button
from random import choice, choices, sample

button_bg_color = "brown2"
bg_color = "RoyalBlue3"
rectangle_fill = "orange"

screen_width = 600
screen_height = 790
square_length = 100
distance_between_squares = 20
padx = (screen_width - 4 * square_length - 3 * distance_between_squares) / 2
pady = 50

digits_vs_textsize = {0: 32, 1: 32, 2: 32, 3: 26, 4: 20, 5: 16, 6: 14}
digits_vs_width = {0: 20, 1: 20, 2: 38, 3: 45.5, 4: 46, 5: 47, 6: 50}
digits_vs_height = {0: 38, 1: 38, 2: 38, 3: 32, 4: 25, 5: 20, 6: 18}
score_label_digits_vs_textsize = {0: 120, 1: 120, 2: 136.5, 3: 153, 4: 169.5, 5: 186, 6: 202.5, 7: 219, 8: 235.5, 9: 252, 10: 268.5, 11: 285, 12: 301.5, 13: 318, 14: 334.5, 15: 351, 16: 367.5, 17: 384, 18: 400.5, 19: 417}


def condition(n, direction):
    if (direction == "Up" and n >= 4) or (direction == "Down" and n <= 11) or (direction == "Right" and n % 4 != 3) or (
            direction == "Left" and n % 4 != 0):
        return True
    return False


def create_new_label():
    global variables_list, labels_list
    if [label for label in variables_list if label.get() == ""]:
        chosen_position = variables_list.index(choice([label for label in variables_list if label.get() == ""]))
        variables_list[chosen_position].set(
            choices([2 ** (n + 1) for n in range(2)], weights=[50 ^ (2 - n) for n in range(2)], k=1)[0])
        labels_list[chosen_position].place(
            x=(square_length + distance_between_squares) * (chosen_position % 4) + padx + square_length / 2 -
              digits_vs_width[len(variables_list[chosen_position].get())],
            y=(square_length + distance_between_squares) * (chosen_position // 4) + pady + square_length/2 - digits_vs_height[len(variables_list[chosen_position].get())])


def move_direction(n, n1, direction):
    global variables_list, labels_list, screen
    while condition(n, direction) and variables_list[n].get() != "" and variables_list[n + n1].get() == "":
        variables_list[n + n1].set(variables_list[n].get())
        variables_list[n].set("")
        labels_list[n].config(font=("Arial", digits_vs_textsize[len(variables_list[n].get())], "bold"))
        labels_list[n+n1].config(font=("Arial", digits_vs_textsize[len(variables_list[n+n1].get())], "bold"))
        labels_list[n + n1].place(x=(square_length + distance_between_squares) * ((n + n1) % 4) + padx + square_length/2 - digits_vs_width[
            len(variables_list[n + n1].get())],
                                  y=(square_length + distance_between_squares) * ((n + n1) // 4) + pady + square_length/2 - digits_vs_height[
            len(variables_list[n + n1].get())])
        n += n1
        screen.after(75)
    while condition(n, direction) and variables_list[n].get() != "" and variables_list[n + n1].get() == variables_list[
        n].get():
        variables_list[n + n1].set(str(int(variables_list[n + n1].get()) * 2))
        score.set(f"Score: {int(score.get().split(': ')[1]) + int(variables_list[n + n1].get())}")
        variables_list[n].set("")
        labels_list[n].config(font=("Arial", digits_vs_textsize[len(variables_list[n].get())], "bold"))
        labels_list[n+n1].config(font=("Arial", digits_vs_textsize[len(variables_list[n+n1].get())], "bold"))
        try:
            labels_list[n + n1].place(x=(square_length + distance_between_squares) * ((n + n1) % 4) + padx + square_length/2 - digits_vs_width[
                len(variables_list[n + n1].get())],
                                      y=(square_length + distance_between_squares) * ((n + n1) // 4) + pady + square_length/2 - digits_vs_height[
                len(variables_list[n + n1].get())])
        except KeyError:
            print(f"Congratulations! You have completed the game with a score of {score.get()}")
            restart_game()
            break
        score_label.place(x=410 - score_label_digits_vs_textsize[len(score.get().split(': ')[1])], y=20)
        n += n1
        screen.after(75)


def move_right(event):
    global variables_list, score
    for number in range(0, 3)[::-1]:
        for row in range(4):
            n = number + 4 * row
            move_direction(n, 1, "Right")
    screen.after(300, create_new_label)


def move_left(event):
    global variables_list, score
    for number in range(1, 4):
        for row in range(4):
            n = number + 4 * row
            move_direction(n, -1, "Left")
    screen.after(300, create_new_label)


def move_up(event):
    global variables_list, score
    for row in range(4, 13, 4):
        for number in range(4):
            n = number + row
            move_direction(n, -4, "Up")
    screen.after(300, create_new_label)


def move_down(event):
    global variables_list, score
    for row in range(0, 9, 4)[::-1]:
        for number in range(4):
            n = number + row
            move_direction(n, 4, "Down")
    screen.after(300, create_new_label)


def restart_game():
    global variables_list
    score.set("Score: 0")
    score_label.place(x=410 - score_label_digits_vs_textsize[len(score.get().split(': ')[1])], y=20)
    for variable in variables_list:
        variable.set("")
    random_choice = sample(variables_list, 2)
    for label in random_choice:
        label.set('2')


screen = Tk()
screen.config(bg=bg_color)
screen.geometry(f"{screen_width}x{screen_height}")

label = Label(fg="goldenrod3", padx=10, pady=20, bg=bg_color, anchor="w", justify="left")
label.config(text=2048, font=("Arial", 36, "bold", "underline"))
label.grid(row=0, column=0, padx=50, sticky="w", columnspan=2)
label = Label(fg="goldenrod", padx=10, bg=bg_color, anchor="w", justify="left")
label.config(text="Join the tiles, get to 2048!", font=("Arial", 16, 'bold'), justify="left")
label.grid(row=1, column=0, columnspan=2, padx=50, sticky="w")

score = StringVar()
score.set("Score: 0")
score_label = Label(fg="goldenrod", padx=10, pady=10, bg=bg_color, justify="center", textvariable=score)
score_label.config(font=("Arial", 30, "bold"))
score_label.place(x=290, y=20)

canvas = Canvas(screen, height=2 * pady + 4 * square_length + 3 * distance_between_squares, width=screen_width,
                bg=bg_color, borderwidth=0, highlightthickness=0)
canvas.grid(row=2, column=0)

labels_list = []
variables_list = []
occupied_list = []
for j in range(0, 4):
    for i in range(0, 4):
        canvas_object = canvas.create_rectangle((square_length + distance_between_squares) * i + padx,
                                                (square_length + distance_between_squares) * j + pady,
                                                (square_length + distance_between_squares) * i + square_length + padx,
                                                (square_length + distance_between_squares) * j + square_length + pady,
                                                fill=rectangle_fill, tags=(f"Row {i}", f"Column {j}"))
        variable = StringVar()
        variable.set("")
        label = Label(canvas, bg=rectangle_fill, font=("Arial", 32, "bold"), fg="black", textvariable=variable,
                      justify="center")
        label.place(x=(square_length + distance_between_squares) * i + 100,
                    y=(square_length + distance_between_squares) * j + 68)
        variables_list.append(variable)
        labels_list.append(label)

random_choice = sample(variables_list, 2)
for variable in random_choice:
    variable.set("2")

restart_button = Button(screen, relief='groove', command=restart_game, bg=button_bg_color,
                        activebackground=button_bg_color)
restart_button.config(text="New Game")
restart_button.grid(row=3, column=0, columnspan=2)

screen.bind('<Up>', move_up)
screen.bind('<Down>', move_down)
screen.bind('<Left>', move_left)
screen.bind('<Right>', move_right)
screen.bind('<w>', move_up)
screen.bind('<s>', move_down)
screen.bind('<a>', move_left)
screen.bind('<d>', move_right)

screen.mainloop()

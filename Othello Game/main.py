from tkinter import Tk, Label, Radiobutton, IntVar, TclError, PhotoImage, Button, Canvas, GROOVE

var = None
CPU_to_play = True
root = None
ask_user_choice_color = "gold"


def ask_multiple_choice_question():
    global var, root
    root = Tk()
    root.config(bg=ask_user_choice_color)
    root.title("Choose your Mode")
    Label(root, text="Choose to play Multiplayer or Against the Computer", background=ask_user_choice_color).pack(pady=10)
    var = IntVar()
    var.set(10)
    for i, option in enumerate(['Multiplayer', 'Computer']):
        Radiobutton(root, text=option, variable=var, value=i, command=check_user_input, background=ask_user_choice_color,  width=50, height=2, anchor="w").pack(anchor="w", pady=5)
    try:
        root.mainloop()
    except (NameError, TclError):
        pass


def check_user_input():
    global var, root, CPU_to_play
    while var.get() != 0 and var.get() != 1:
        ask_multiple_choice_question()
    if var.get() == 0:
        CPU_to_play = False
    elif var.get() == 1:
        CPU_to_play = True
    try:
        root.destroy()
    except (NameError, TclError):
        pass


ask_multiple_choice_question()

check_user_input()

screen_height = 900
screen_width = 1200
square_length = 100

# TODO Change the white_coin and black_coin icons.
# TODO Code to Restart the game

screen = Tk()
screen.title("Othello Game")
screen.config(bg="OliveDrab4")
screen.geometry(f"{screen_width}x{screen_height}")

rectangle_fill = "brown3"

white_coin = PhotoImage(file="white_coin.png")
white_coin = white_coin.subsample(white_coin.width() // 80, white_coin.height() // 80)
black_coin = PhotoImage(file="black_coin.png")
black_coin = black_coin.subsample(black_coin.width() // 80, black_coin.height() // 80)
indicator = PhotoImage(file="indicator.png")
indicator = indicator.subsample(indicator.width()//120, indicator.width()//120)


def check_list(list_of_buttons, button, only_check=False, check_for_valid_move=False, CPU_play=False):
    global white_buttons_list, black_buttons_list, black_to_play
    length_list = []
    initial_number = list_of_buttons.index(button)
    number = initial_number
    if not black_to_play:
        player1_list = white_buttons_list
        player2_list = black_buttons_list
        player1_image = white_coin
    if black_to_play:
        player1_list = black_buttons_list
        player2_list = white_buttons_list
        player1_image = black_coin
    if initial_number != 0:
        number -= 1
        while list_of_buttons[number] in player2_list and number != 0:
            number -= 1
        if CPU_play and list_of_buttons[number] in player1_list and abs(number - initial_number) > 1:
            length_list.append([list_of_buttons, initial_number, number, abs(number - initial_number), buttons_list.index(button)])
        if not only_check and not check_for_valid_move and not CPU_play and list_of_buttons[number] in player1_list:
            for button in [button for button in list_of_buttons[number: initial_number] if button in player2_list]:
                button.config(image="")
                button.config(image=player1_image)
                player2_list.remove(button)
                player1_list.append(button)
        elif only_check and not CPU_play and list_of_buttons[number] not in player2_list and list_of_buttons[number] not in player1_list and abs(number-initial_number) != 1:
            return True
        elif check_for_valid_move and not CPU_play and list_of_buttons[number] in player1_list and abs(number-initial_number) != 1:
            return True
        number = initial_number
    if initial_number != len(list_of_buttons) - 1:
        number += 1
        while list_of_buttons[number] in player2_list and number != len(list_of_buttons) - 1:
            number += 1
        if CPU_play and list_of_buttons[number] in player1_list and abs(number - initial_number) > 1:
            length_list.append([list_of_buttons, initial_number, number, abs(number - initial_number), buttons_list.index(button)])
        if not only_check and not check_for_valid_move and not CPU_play and list_of_buttons[number] in player1_list:
            for button in [button for button in list_of_buttons[initial_number: number] if button in player2_list]:
                button.config(image="")
                button.config(image=player1_image)
                player2_list.remove(button)
                player1_list.append(button)
        elif only_check and not CPU_play and list_of_buttons[number] not in player2_list and list_of_buttons[number] not in player1_list  and abs(number-initial_number) != 1:
            return True
        elif check_for_valid_move and not CPU_play and list_of_buttons[number] in player1_list and abs(number-initial_number) != 1:
            return True
    if only_check or check_for_valid_move:
        return False
    if CPU_play and length_list:
        absolute_differences = [element[-2] for element in length_list]
        return length_list[absolute_differences.index(max(absolute_differences))]
    if CPU_play and not length_list:
        return [[0], 0, 0, 0]


def check_if_can_outflank(number, only_check=False, check_for_valid_move=False):
    row_number = number // 8
    column_number = number % 8
    for list_of_buttons in [buttons_list[8 * row_number: 8 * row_number + 8],
                            buttons_list[column_number: column_number + 64: 8],
                            buttons_list[
                            number - 9 * min(row_number, column_number): number + 9 * min(7 - row_number, 7 -
                                                                                                          column_number) + 1:9],
                            buttons_list[number - 7 * row_number:number + 7 * column_number + 1: 7]]:
        if check_list(list_of_buttons, buttons_list[number], only_check=only_check, check_for_valid_move=check_for_valid_move):
            return True
    return False


def check_if_switch_sides():
    global black_to_play
    if (not black_to_play and not black_buttons_list) or (black_to_play and not white_buttons_list):
        black_to_play = not black_to_play
    elif black_to_play and not any(
            [check_if_can_outflank(buttons_list.index(black_button), only_check=True) for black_button in black_buttons_list]):
        black_to_play = False
    elif not black_to_play and not any(
            [check_if_can_outflank(buttons_list.index(white_button), only_check=True) for white_button in white_buttons_list]):
        black_to_play = True
    if black_to_play:
        indicator_button.place(x=1050, y=700)
    if not black_to_play:
        indicator_button.place(x=50, y=700)

def button_clicked(button):
    global black_to_play, white_coin, black_coin, white_buttons_list, black_buttons_list
    if button not in white_buttons_list and button not in black_buttons_list and check_if_can_outflank(buttons_list.index(button), check_for_valid_move=True):
        if not black_to_play:
            button.config(image=white_coin)
            white_buttons_list.append(button)
        elif black_to_play:
            button.config(image=black_coin)
            black_buttons_list.append(button)
        number = buttons_list.index(button)
        row_number = number // 8
        column_number = number % 8
        for list_of_buttons in [buttons_list[8 * row_number: 8 * row_number + 8],
                                buttons_list[column_number: column_number + 64: 8],
                                buttons_list[
                                number - 9 * min(row_number, column_number): number + 9 * min(7 - row_number, 7 -
                                                                                                              column_number) + 1:9],
                                buttons_list[number - 7 * row_number:number + 7 * column_number + 1: 7]]:
            check_list(list_of_buttons, buttons_list[number])
        black_to_play = not black_to_play
        if len(white_buttons_list) + len(black_buttons_list) != len(buttons_list):
            check_if_switch_sides()
        elif len(white_buttons_list) > len(black_buttons_list):
            print(f"Game Over. The winner is White")
        elif len(white_buttons_list) < len(black_buttons_list):
            print(f"Game Over. The winner is Black")
        elif len(white_buttons_list) == len(black_buttons_list):
            print("Game over. The game resulted in a draw.")
        if not black_to_play and CPU_to_play:
            screen.after(750, computer_play)



def computer_play():
    global white_buttons_list, buttons_list, black_to_play
    length_list = []
    for number in [buttons_list.index(button) for button in buttons_list if button not in white_buttons_list and button not in black_buttons_list]:
        row_number = number//8
        column_number = number%8
        for list_of_buttons in [buttons_list[8 * row_number: 8 * row_number + 8],
                                buttons_list[column_number: column_number + 64: 8],
                                buttons_list[
                                number - 9 * min(row_number, column_number): number + 9 * min(7 - row_number, 7 -
                                                                                                              column_number) + 1:9],
                                buttons_list[number - 7 * row_number:number + 7 * column_number + 1: 7]]:
            length_list.append(check_list(list_of_buttons, buttons_list[number], CPU_play=True))
    absolute_differences = [element[-2] for element in length_list]
    if max(absolute_differences) != 0:
        best_move = length_list[absolute_differences.index(max(absolute_differences))]
        minimum = min(best_move[1], best_move[2])
        maximum = max(best_move[1], best_move[2])
        for button in best_move[0][minimum: maximum + 1]:
            if button not in white_buttons_list:
                button.config(image="")
                button.config(image=white_coin)
                if button in black_buttons_list:
                    black_buttons_list.remove(button)
                white_buttons_list.append(button)
    black_to_play = True
    indicator_button.place(x=1050, y=700)
    if len(white_buttons_list) + len(black_buttons_list) != len(buttons_list):
        check_if_switch_sides()
    elif len(white_buttons_list) > len(black_buttons_list):
        print(f"Game Over. The winner is White")
    elif len(white_buttons_list) < len(black_buttons_list):
        print(f"Game Over. The winner is Black")
    elif len(white_buttons_list) == len(black_buttons_list):
        print("Game over. The game resulted in a draw.")


white_coin_button = Button(screen, bg="OliveDrab4", image=white_coin, activebackground="OliveDrab4", highlightthickness=0, borderwidth=0)
white_coin_button.place(x=50, y=700)
black_coin_button = Button(screen, bg="OliveDrab4", image=black_coin, activebackground="OliveDrab4", highlightthickness=0, borderwidth=0)
black_coin_button.place(x=1050, y=700)
indicator_button = Button(screen, bg="OliveDrab4", image=indicator, activebackground="OliveDrab4", highlightthickness=0, borderwidth=0)


canvas = Canvas(screen, height=8 * square_length, width=8 * square_length, bg="brown3")
canvas.grid(row=1, column=0, pady=(screen_height - 8 * square_length) / 2, padx=(screen_width - 8 * square_length) / 2)
buttons_list = []
white_buttons_list = []
black_buttons_list = []
variables_list = []
for j in range(0, 8):
    for i in range(0, 8):
        canvas_object = canvas.create_rectangle(square_length * i,
                                                square_length * j,
                                                square_length * (i + 1),
                                                square_length * (j + 1),
                                                fill=rectangle_fill, tags=(f"Row {i}", f"Column {j}"))
        token = Button(canvas, highlightthickness=1, relief=GROOVE, width=100, height=100, activebackground="brown3",
                       background="brown3")
        token.config(command=lambda button=token: button_clicked(button))
        if (i, j) == (3, 3) or (i, j) == (4, 4):
            token.config(image=white_coin)
            white_buttons_list.append(token)
        elif (i, j) == (3, 4) or (i, j) == (4, 3):
            token.config(image=black_coin)
            black_buttons_list.append(token)
        token.place(x=square_length * i, y=square_length * j)
        buttons_list.append(token)

black_to_play = True
indicator_button.place(x=1050, y=700)

screen.mainloop()

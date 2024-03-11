from tkinter import *
from tkinter.ttk import Combobox

bg_color = "DodgerBlue2"


class MatrixCanvas(Canvas):
    def __init__(self, screen, canvas_type="Primary"):
        super().__init__(screen)
        self.screen = screen
        self.number_of_rows = IntVar()
        self.number_of_rows.set(3)
        self.number_of_columns = IntVar()
        self.number_of_columns.set(3)
        if canvas_type == "Primary":
            self.nrows = Dimensions_Spinbox(self, spinbox_number=1, textvariable=self.number_of_rows)
            self.ncolumns = Dimensions_Spinbox(self, spinbox_number=2, textvariable=self.number_of_columns)
            self.config(width=750, height=800, bg=bg_color, borderwidth=0, highlightthickness=0)
        else:
            self.nrows = Dimensions_Spinbox(self, spinbox_number=3, textvariable=self.number_of_rows)
            self.ncolumns = Dimensions_Spinbox(self, spinbox_number=4, textvariable=self.number_of_columns)
            self.config(width=750, height=450, bg=bg_color, borderwidth=0, highlightthickness=0)
        self.button = Button(self, activebackground="blue", background="blue")
        self.reset_button = Button(self, activebackground="blue", background="blue", text="Clear", command=self.reset_matrix)
        self.dict = {}


    def fullsize(self):
        self.config(width=730, height=800)
        self.nrows.config(from_=1, to=14)
        self.ncolumns.config(from_=1, to=14)
        self.screen.update()
        self.nrows.place(x=self.winfo_width() / 2 - 140, y=0)
        self.ncolumns.place(x=self.winfo_width() / 2 + 70, y=0)
        # self.button.pack(side=BOTTOM, pady=10)
        self.button.place(relx=0.8, rely=0.98, x=0, y=0, anchor=SE)
        self.reset_button.place(rely=0.98, relx=0.2, x=0, y=0, anchor=SW)


    def smallsize(self):
        self.config(width=750, height=400)
        self.pack()
        self.button.pack_forget()
        self.button.place_forget()
        self.reset_button.place(rely=0.98, relx=0.46, x=0, y=0, anchor=SW)
        self.nrows.config(to=7)
        self.ncolumns.config(to=7)
        self.screen.update()
        self.nrows.place(x=self.winfo_width() / 2 - 140, y=0)
        self.ncolumns.place(x=self.winfo_width() / 2 + 70, y=0)


    def reset_matrix(self):
        for key, values in self.dict.items():
            values["Variable"].set("")


class Dimensions_Spinbox(Spinbox):
    def __init__(self, canvas, spinbox_number, textvariable):
        super().__init__(canvas, justify=CENTER, textvariable=textvariable, width=5)
        if spinbox_number < 3:
            self.config(from_=1, to=14)
        else:
            self.config(from_=1, to=7)


class QuestionMenu(Combobox):
    def __init__(self, screen, textvariable):
        self.options_list = ["Determinant", "Inverse", "Solve Linear Equation", "Multiply", "Add", "Subtract",
                             'Transpose']
        super().__init__(screen, exportselection=False, textvariable=textvariable, justify="center",
                         values=self.options_list, state="readonly")
        self.pack(pady=40)


class ResultCanvas(Canvas):
    def __init__(self, screen):
        super().__init__(screen, bg=bg_color, borderwidth=0, highlightthickness=0)
        self.label = Label(self, font="Arial 18 bold", wraplength=600, background=bg_color, text="")
        self.label.pack()
        self.config(width=750, height=800)
        self.entries_dict = []
        self.revert_button = Button(self, activebackground="blue", background="blue", text="Return to Home")
        self.revert_button.pack(side=BOTTOM, pady=100)


def only_include_digits(variable):
    variable.set("".join([digit for digit in variable.get().strip() if
                          digit.isdigit() or (digit == "-" and variable.get().index(digit) == 0) or digit == "."]))
    if variable.get().count(".") > 1:
        variable.set("".join(variable.get()[::-1].replace(".", "", 1))[::-1])


def return_to_home(entries_canvas, entries_canvas2, results_canvas, user_choice):
    results_canvas.pack_forget()
    entries_canvas.pack()
    entries_canvas.pack_propagate(0)
    if user_choice in ["Add", "Subtract", "Multiply"]:
        entries_canvas2.pack()
        entries_canvas2.pack_propagate(0)


def display_on_results_canvas(results_canvas, matrix, user_choice):
    if matrix is not None and isinstance(matrix, list):
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])

        side_length = 3750 // (6 * number_of_columns - 1)

        for i in range(0, number_of_rows):
            for j in range(0, number_of_columns):
                if matrix[i][j] == int(matrix[i][j]):
                    entry = Label(results_canvas, bg='gold', justify=CENTER, relief=GROOVE, width=side_length // 12,
                                  text=str(int(matrix[i][j])))
                else:
                    entry = Label(results_canvas, bg='gold', justify=CENTER, relief=GROOVE, width=side_length // 12,
                                  text=str(matrix[i][j]))
                entry.place(x=25 + 6 / 5 * side_length * j, y=50 + 50 * i)
                results_canvas.entries_dict.append(entry)

    elif matrix is None and user_choice == "Inverse":
        results_canvas.label.config(foreground="red",
                                    text="The Matrix you have given is singular. No Inverse can be found.")

    elif matrix is None and user_choice == 'Solve Linear Equation':
        results_canvas.label.config(foreground="red", text="No Solution exists for the given set of linear equations.")

    elif isinstance(matrix, float) or isinstance(matrix, int):
        if matrix == int(matrix):
            matrix = int(matrix)
        results_canvas.label.config(text=f"Determinant is: {matrix}")


def create_entries(canvas_to_use, dictionary):
    rows_number = canvas_to_use.number_of_rows.get()
    columns_number = canvas_to_use.number_of_columns.get()
    side_length = 3750 // (6 * columns_number)

    for entry in dictionary.values():
        if entry['row'] > rows_number - 1 or entry['column'] > columns_number - 1:
            entry['Entry'].place_forget()

    for i in range(0, rows_number):
        for j in range(0, columns_number):
            if dictionary.get(f"Row {i} Column {j}") is not None:
                dictionary[f"Row {i} Column {j}"]["Entry"].config(width=side_length // 12)
                initial_number = dictionary[f"Row {i} Column {j}"]["Variable"].get()
                dictionary[f"Row {i} Column {j}"]["Entry"].delete(0, END)
                dictionary[f"Row {i} Column {j}"]["Entry"].insert(0, initial_number)
                dictionary[f"Row {i} Column {j}"]["Entry"].place(x=6 / 5 * side_length * j, y=50 + 50 * i)
            else:
                variable = StringVar()
                variable.set("")
                variable.trace_add("write", lambda _a, _b, _c, var=variable: only_include_digits(var))
                entry = Entry(canvas_to_use, bg='gold', justify=CENTER, relief=GROOVE, textvariable=variable,
                              width=side_length // 12)
                entry.bind('<Up>',
                           lambda event, row=i, column=j, move_direction="Up",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                entry.bind('<Down>',
                           lambda event, row=i, column=j, move_direction="Down",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                entry.bind('<Left>',
                           lambda event, row=i, column=j, move_direction="Left",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                entry.bind('<Right>',
                           lambda event, row=i, column=j, move_direction="Right",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                entry.bind('<w>',
                           lambda event, row=i, column=j, move_direction="Up",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                entry.bind('<s>',
                           lambda event, row=i, column=j, move_direction="Down",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                entry.bind('<a>',
                           lambda event, row=i, column=j, move_direction="left",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                entry.bind('<d>',
                           lambda event, row=i, column=j, move_direction="Right",
                                  canvas=canvas_to_use, dictionary=dictionary, rows_number=rows_number,
                                  columns_number=columns_number: move_to_new_cell(event, row, column,
                                                                                  move_direction, dictionary,
                                                                                  canvas_to_use))
                # entry.bind('<Enter>', lambda event, row=i, column=j, move_direction="Next": move_to_new_cell(event, row, column, move_direction))
                entry.place(x=6 / 5 * side_length * j, y=50 + 50 * i)
                dictionary[f"Row {i} Column {j}"] = {"Entry": entry, "Variable": variable, "row": i, "column": j}
    dictionary["Row 0 Column 0"]["Entry"].focus()
    dictionary["Row 0 Column 0"]["Entry"].icursor(END)


def move_to_new_cell(event, row, column, move_direction, dictionary, entry_canvas):
    rows_number = entry_canvas.number_of_rows.get()
    columns_number = entry_canvas.number_of_columns.get()
    if move_direction == "Right" and column < columns_number - 1 and \
            dictionary[f"Row {row} Column {column}"]["Entry"].index(INSERT) == len(
            dictionary[f"Row {row} Column {column}"]["Variable"].get()):
        dictionary[f"Row {row} Column {column + 1}"]["Entry"].focus()
        dictionary[f"Row {row} Column {column + 1}"]["Entry"].icursor(END)
    if move_direction == "Left" and column > 0 and dictionary[f"Row {row} Column {column}"]["Entry"].index(
            INSERT) == 0:
        dictionary[f"Row {row} Column {column - 1}"]["Entry"].focus()
        dictionary[f"Row {row} Column {column - 1}"]["Entry"].icursor(END)
    if move_direction == "Up" and row > 0:
        dictionary[f"Row {row - 1} Column {column}"]["Entry"].focus()
        dictionary[f"Row {row - 1} Column {column}"]["Entry"].icursor(END)
    if move_direction == "Down" and row < rows_number - 1:
        dictionary[f"Row {row + 1} Column {column}"]["Entry"].focus()
        dictionary[f"Row {row + 1} Column {column}"]["Entry"].icursor(END)

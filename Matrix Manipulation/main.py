from calculations import *
from gui import *

bg_color = "DodgerBlue2"
screen = Tk()
# A geometry of 1000 along y almost entirely fills up this screen. This may vary for other computers.
# I personally found it better to keep the geometry just below the full screen size.
screen.geometry("800x1000")
screen.config(bg=bg_color)

user_choice = StringVar()
user_choice.set("Select an Option")


def display_resultant_matrix(matrix):
    global entries_canvas, entries_canvas2, results_canvas, user_choice
    entries_canvas.pack_forget()
    entries_canvas2.place_forget()
    entries_canvas2.pack_forget()
    results_canvas.label.config(text="", fg="black")
    results_canvas.pack(fill=BOTH, expand=YES)
    for entry in results_canvas.entries_dict:
        entry.destroy()

    display_on_results_canvas(results_canvas, matrix, user_choice.get())


def Spinbox_clicked(user_choice, spinbox_number=None, canvas=1):
    if user_choice in ['Inverse', 'Determinant']:
        if spinbox_number == 1:
            entries_canvas.number_of_columns.set(entries_canvas.number_of_rows.get())
        if spinbox_number == 2:
            entries_canvas.number_of_rows.set(entries_canvas.number_of_columns.get())
    if user_choice == 'Solve Linear Equation':
        if spinbox_number == 1:
            entries_canvas.number_of_columns.set(entries_canvas.number_of_rows.get() + 1)
        if spinbox_number == 2:
            entries_canvas.number_of_rows.set(entries_canvas.number_of_columns.get() - 1)
    if user_choice in ["Add", "Subtract"]:
        if spinbox_number == 1:
            entries_canvas2.number_of_rows.set(entries_canvas.number_of_rows.get())
        if spinbox_number == 2:
            entries_canvas2.number_of_columns.set(entries_canvas.number_of_columns.get())
        if spinbox_number == 3:
            entries_canvas.number_of_rows.set(entries_canvas2.number_of_rows.get())
        if spinbox_number == 4:
            entries_canvas.number_of_columns.set(entries_canvas2.number_of_columns.get())
    if user_choice == "Multiply":
        if spinbox_number == 2:
            entries_canvas2.number_of_rows.set(entries_canvas.number_of_columns.get())
        if spinbox_number == 3:
            entries_canvas.number_of_columns.set(entries_canvas2.number_of_rows.get())

    if canvas == 1 or spinbox_number in [1, 2]:
        create_entries(entries_canvas, entries_canvas.dict)
    if canvas == 2 or spinbox_number in [3, 4] or (spinbox_number in [1, 2] and user_choice in ["Add", "Subtract"]):
        create_entries(entries_canvas2, entries_canvas2.dict)


def initiate_calculation(event):
    global user_choice, entries_canvas, entries_canvas2
    return_to_home(entries_canvas, entries_canvas2, results_canvas, user_choice.get())

    # Broad Functionality
    if user_choice.get() in ['Transpose', 'Inverse', 'Determinant', 'Solve Linear Equation']:
        entries_canvas.fullsize()
        entries_canvas2.place_forget()
        entries_canvas2.pack_forget()
    elif user_choice.get() in ['Add', 'Subtract', 'Multiply']:
        entries_canvas.smallsize()
        entries_canvas2.place(x=25, y=520)
        screen.update()
        entries_canvas2.nrows.place(x=entries_canvas2.winfo_width() / 2 - 140, y=0)
        entries_canvas2.ncolumns.place(x=entries_canvas2.winfo_width() / 2 + 70, y=0)
        entries_canvas2.reset_button.place(rely=0.98, relx=0.2, x=0, y=0, anchor=SW)

    # Specific Functionality
    if user_choice.get() == 'Transpose':
        Spinbox_clicked(user_choice=user_choice.get())
        entries_canvas.button.config(text="Transpose",
                                     command=lambda: display_resultant_matrix(transpose(matrix=matrix_from_dict(entries_canvas))))

    elif user_choice.get() == 'Inverse':
        entries_canvas.number_of_columns.set(entries_canvas.number_of_rows.get())
        Spinbox_clicked(user_choice=user_choice.get())
        entries_canvas.button.config(text="Inverse", command=lambda: display_resultant_matrix(inverse(matrix=matrix_from_dict(entries_canvas))))

    elif user_choice.get() == 'Determinant':
        entries_canvas.number_of_columns.set(entries_canvas.number_of_rows.get())
        Spinbox_clicked(user_choice=user_choice.get())
        entries_canvas.button.config(text='Determinant',
                                     command=lambda: display_resultant_matrix(det_matrix(matrix=matrix_from_dict(entries_canvas))))

    elif user_choice.get() == 'Solve Linear Equation':
        entries_canvas.number_of_columns.set(entries_canvas.number_of_rows.get() + 1)
        entries_canvas.ncolumns.config(from_=2, to=15)
        Spinbox_clicked(user_choice=user_choice.get())
        entries_canvas.button.config(text="Solve",
                                     command=lambda: display_resultant_matrix(solve_linear_equation(matrix=matrix_from_dict(entries_canvas))))

    elif user_choice.get() == "Add":
        entries_canvas2.number_of_columns.set(entries_canvas.number_of_columns.get())
        entries_canvas2.number_of_rows.set(entries_canvas.number_of_rows.get())
        Spinbox_clicked(user_choice=user_choice.get())
        Spinbox_clicked(user_choice=user_choice.get(), canvas=2)
        entries_canvas2.button.config(text="Add", command=lambda: display_resultant_matrix(
                matrix_sum(matrix1=matrix_from_dict(entries_canvas), matrix2=matrix_from_dict(entries_canvas2))))
        entries_canvas2.button.place(relx=0.8, rely=0.98, x=0, y=0, anchor=SE)

    elif user_choice.get() == "Subtract":
        entries_canvas2.number_of_columns.set(entries_canvas.number_of_columns.get())
        entries_canvas2.number_of_rows.set(entries_canvas.number_of_rows.get())
        Spinbox_clicked(user_choice=user_choice.get())
        Spinbox_clicked(user_choice=user_choice.get(), canvas=2)
        entries_canvas2.button.config(text="Subtract", command=lambda: display_resultant_matrix(
            matrix_difference(matrix1=matrix_from_dict(entries_canvas), matrix2=matrix_from_dict(entries_canvas2))))
        entries_canvas2.button.place(relx=0.8, rely=0.98, x=0, y=0, anchor=SE)

    elif user_choice.get() == 'Multiply':
        entries_canvas2.number_of_rows.set(entries_canvas.number_of_columns.get())
        Spinbox_clicked(user_choice=user_choice.get())
        Spinbox_clicked(user_choice=user_choice.get(), canvas=2)
        entries_canvas2.button.config(text="Multiply", command=lambda: display_resultant_matrix(multiply_matrix(matrix1=matrix_from_dict(entries_canvas), matrix2=matrix_from_dict(entries_canvas2))))
        entries_canvas2.button.place(relx=0.8, rely=0.98, x=0, y=0, anchor=SE)


question_menu = QuestionMenu(screen, user_choice)
question_menu.bind("<<ComboboxSelected>>", initiate_calculation)

entries_canvas = MatrixCanvas(screen)
entries_canvas.pack()
entries_canvas.pack_propagate(0)
entries_canvas2 = MatrixCanvas(screen, canvas_type="Secondary")

entries_canvas.nrows.config(command=lambda: Spinbox_clicked(user_choice=user_choice.get(), spinbox_number=1))
entries_canvas.ncolumns.config(command=lambda: Spinbox_clicked(user_choice=user_choice.get(), spinbox_number=2))
entries_canvas2.nrows.config(command=lambda: Spinbox_clicked(user_choice=user_choice.get(), spinbox_number=3))
entries_canvas2.ncolumns.config(command=lambda: Spinbox_clicked(user_choice=user_choice.get(), spinbox_number=4))

results_canvas = ResultCanvas(screen)
results_canvas.config(width=7500, height=8000)
results_canvas.revert_button.config(
    command=lambda: return_to_home(entries_canvas, entries_canvas2, results_canvas, user_choice.get()))

screen.mainloop()

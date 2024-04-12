import json
from tkinter import *
from tkinter import messagebox
from quizmaster import QuizMaster

with open("categories_data.json") as file:
    categories_data = json.load(file)


def number_of_questions_changed(var):
    global category, number_of_questions, initial_number_of_questions, initial_category
    if quiz_master.score != 0:
        message_box = messagebox.askokcancel(title="Confirm Changing Number of Questions", message="Are you sure you want to change the number of questions?", default="cancel")
    else:
        message_box = True
    if message_box:
        initial_number_of_questions = number_of_questions.get()
        ask_category['menu'].delete(0, 'end')
        for choice in [category for category, data in categories_data.items() if data['number_of_questions'] >= int(number_of_questions.get())]:
            ask_category['menu'].add_command(label=choice, command=lambda value=choice: category.set(value))
        category.set("Any Category")
        initial_category = category.get()
        quiz_master.display_questions(number_of_questions.get(), category.get())
    if not message_box:
        number_of_questions.set(initial_number_of_questions)

def category_changed(*args):
    global category, number_of_questions, initial_category
    if quiz_master.score != 0:
        message_box = messagebox.askokcancel(title="Confirm Changing Category", message="Are you sure you want to change category", default="cancel")
    else:
        message_box = True
    if message_box:
        initial_category = category.get()
        quiz_master.display_questions(number_of_questions.get(), category.get())
    if not message_box:
        category.set(initial_category)

screen = Tk()
screen.title("Welcome to the Quiz Game")
screen.config(bg="blue2")
screen.geometry("600x900")

number_of_questions = StringVar()
number_of_questions.set('10')
options = [10, 20, 30, 40, 50]
initial_number_of_questions = '10'
ask_number_of_questions = OptionMenu(screen, number_of_questions, *options, command=number_of_questions_changed)
ask_number_of_questions.pack(pady=20)

category = StringVar()
category.set('Any Category')
category.trace('w', category_changed)
category_options = [category for category, data in categories_data.items() if data['number_of_questions'] >= int(number_of_questions.get())]
initial_category = 'Any Category'
ask_category = OptionMenu(screen, category, *category_options)
ask_category.pack(pady=20)

quiz_master = QuizMaster(screen)
quiz_master.display_questions(number_of_questions.get(), category.get())

screen.mainloop()

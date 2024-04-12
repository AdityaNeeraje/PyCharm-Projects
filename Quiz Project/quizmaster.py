import json
import requests
from html import unescape
from tkinter import *
from tkinter import messagebox
from random import shuffle

url = "https://opentdb.com/api.php"
with open("categories_data.json", "r") as file:
    categories_data = json.load(file)

with open("high_scores_data.json", "r") as file:
    high_scores_dict = json.load(file)


class QuizMaster:
    def __init__(self, screen):
        self.score = 0
        self.high_score = 0
        self.questions_attempted = 0
        self.questions = []
        self.correct_answers = []
        self.screen = screen

        self.score_label = Label(screen, fg="black", font=("Arial", 14, "bold"), bg="blue2")
        self.score_label.place(x=70, y=160)
        self.high_score_label = Label(screen, fg="black", font=("Arial", 14, "bold"), bg="blue2")
        self.high_score_label.place(x=400, y=160)
        self.canvas = Canvas(screen)
        self.canvas.pack(pady=100)
        self.question_label = Label(self.canvas, wraplength=325, font=("Arial", 22, "bold"), justify="center", bg="LemonChiffon2")
        self.question_label.place(relx=0.5, rely=0.5, anchor="center")
        self.canvas.config(width=400, height=400)
        self.screen.pack_propagate(0)
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self.screen, command=lambda: self.check_answer('True'), borderwidth=0,
                                  image=self.true_image)
        self.true_button.place(x=100, y=700)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self.screen, command=lambda: self.check_answer('False'), borderwidth=0,
                                   image=self.false_image)
        self.false_button.place(x=400, y=700)
        self.buttons_disabled = True

    def display_questions(self, number_of_questions, category):
        self.number_of_questions = int(number_of_questions)
        self.category = category
        if category == "Any Category":
            params = {
                "amount": self.number_of_questions,
                "type": "boolean",
            }
        else:
            params = {
                "amount": self.number_of_questions,
                "category": categories_data[category]["id"],
                "type": "boolean",
            }
        response = requests.get(url, params=params).json()
        if response['response_code'] != 0:
            print(
                "Unable to successfully make an API call. Check the OpenTB documentation to ensure there are no changes in the relevant API documentation.")
        else:
            questions_list = response['results']
            shuffle(questions_list)
            self.questions = [unescape(question["question"]) for question in questions_list]
            self.correct_answers = [question["correct_answer"] for question in questions_list]
            self.score = 0
            self.questions_attempted = 0
            self.high_score = high_scores_dict[number_of_questions][category]
            self.score_label.config(text=f"Score: {self.score}/{self.questions_attempted}")
            self.high_score_label.config(text=f"High Score: {self.high_score}")
            self.ask_questions()

    def ask_questions(self):
        self.buttons_disabled = False
        self.canvas.config(bg="LemonChiffon2")
        self.question_label.config(text=self.questions[0], bg="LemonChiffon2")

    def check_answer(self, boolean):
        if not self.buttons_disabled:
            self.buttons_disabled = True
            self.questions_attempted += 1
            if self.correct_answers[0] == boolean:
                self.score += 1
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.high_score_label.config(text=f"High Score: {self.high_score}")
                    high_scores_dict[str(self.number_of_questions)][self.category] = self.high_score
                    with open("high_scores_data.json", "w") as file:
                        json.dump(high_scores_dict, file, indent=4)
                self.canvas.config(bg="green2")
                self.question_label.config(bg="green2")
            else:
                self.canvas.config(bg="red2")
                self.question_label.config(bg="red2")
            self.score_label.config(text=f"Score: {self.score}/{self.questions_attempted}")
            self.screen.after(2000, self.ask_next_question)

    def ask_next_question(self):
        self.questions.remove(self.questions[0])
        self.correct_answers.remove(self.correct_answers[0])
        if self.questions_attempted != self.number_of_questions:
            self.ask_questions()
        else:
            self.canvas.config(bg="LemonChiffon2")
            self.question_label.config(bg="LemonChiffon2",
                text=f"Congratulations! You have successfully answered {self.score} questions. Play again to beat your score.")
            play_again = messagebox.askyesno(title="Congratulations! Quiz complete", message="Do you want to play again?", default="yes")
            if play_again:
                self.display_questions(str(self.number_of_questions), self.category)
            else:
                self.screen.bye()

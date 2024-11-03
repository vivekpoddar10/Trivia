from tkinter import *
from quiz import Quiz

# BG Color Constant
THEME_COLOR = "#375362"

class QuizInterface:
    # Initializing Tkinter in class constructor
    def __init__(self, quiz: Quiz):
        self.quiz = quiz

        # Window
        self.window = Tk()
        self.window.title('Trivia')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # Score Label
        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, highlightthickness=0, fg='white')
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            text='Some Question',
            width=250,
            font=('arial', 20, 'italic'),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Button
        self.false_image = PhotoImage(file='./images/false.png')
        self.false_btn = Button(image=self.false_image, command=self.user_says_incorrect)
        self.false_btn.grid(row=2, column=0)

        self.true_image = PhotoImage(file='./images/true.png')
        self.true_btn = Button(image=self.true_image, command=self.user_says_correct)
        self.true_btn.grid(row=2, column=1)

        # Updating the Canvas text with a question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # check Quiz object still has Question
        self.canvas.config(bg='White')
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = next_question, fill=THEME_COLOR)
        else:
            # Game Over
            msg = f'Game Over! Your score {self.quiz.score} / {self.quiz.question_number}'
            self.canvas.itemconfig(self.question_text, text= msg)
            self.quiz.score = -1
            self.score_label.config(text='')

    # User press the '✔️' button
    def user_says_correct(self):
        if self.quiz.score != -1:
            self.give_feedback('True')

    # User press the '❌' button
    def user_says_incorrect(self):
        if self.quiz.score != -1:
            self.give_feedback('False')

    # Check whether user has selected correct answer and update the screen and score
    def give_feedback(self, user_answer):
        if self.quiz.check_answer(user_answer):
            self.canvas.config(bg='Green')
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)







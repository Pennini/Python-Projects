from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(
            text="Score: 0", font=("Arial", 10, "normal"), bg=THEME_COLOR, fg="white"
        )
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            text="Hello",
            font=("Arial", 18, "italic"),
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        true_img = PhotoImage(file="images/true.png")
        self.correct = Button(
            image=true_img, highlightthickness=0, bg=THEME_COLOR, command=self.is_true
        )
        self.correct.grid(column=1, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.wrong = Button(
            image=false_img, highlightthickness=0, bg=THEME_COLOR, command=self.is_false
        )
        self.wrong.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question, text="You've reached the end of the quiz."
            )
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def is_true(self):
        boolean = self.quiz.check_answer("true")
        self.give_feedback(boolean)

    def is_false(self):
        boolean = self.quiz.check_answer("false")
        self.give_feedback(boolean)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

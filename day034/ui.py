from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_NAME = "Ariel"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)



        self.score_text = Label(text=f"score: 0", font=(FONT_NAME, 15, "bold"))
        self.score_text.config(bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250,  highlightthickness=0)
        self.question_text = self.canvas.create_text(145, 130, width=280, text="00:00", font=(FONT_NAME, 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)



        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_ans)
        self.false_button.grid(column=1, row=2)

        true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_ans)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end, final score {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_ans(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score_text.config(text=f"score: {self.quiz.score}")


    def false_ans(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.score_text.config(text=f"score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



from tkinter import *
from trivia_engine import TriviaEngine

class TriviaUI:
    # Instantaite the game
    def __init__(self, trivia_engine: TriviaEngine):
        self.game = trivia_engine

        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(padx=20, pady=20, bg="white")

        # Score
        self.score_label = Label(text= "Score: 0", fg="black", bg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=300,
            text="Sample text",
            fill="blue",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady= 50)

        # Buttons
        correct = PhotoImage(file="correct.png")
        wrong = PhotoImage(file="wrong.png")
        self.correct_button = Button(image=correct, highlightthickness=0, command=self.correct_pressed)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column=1)

        # Start the game
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        # If there are remaining questions - continue the game
        if self.game.rem_questions():
            self.score_label.config(text=f'Score: {self.game.score}')
            q_text = self.game.get_next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        # Otherwise, end the game
        else:
            self.canvas.itemconfig(self.question_text, text="Game over!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    # Check if the answer is correct or wrong
    def correct_pressed(self):
        self.feedback(self.game.check_answer("True"))

    def wrong_pressed(self):
        self.feedback(self.game.check_answer("False"))

    # Give feedback to the user
    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1500, self.get_next_question)


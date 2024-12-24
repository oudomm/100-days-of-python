from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_lebel = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_lebel.grid(row=0, column=1)

        # Question
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.create_text(
            150,
            125,
            fill="black",
            text="Some Question Text",
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.true_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.true_img, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.false_img, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=2, column=1)

        self.window.mainloop()


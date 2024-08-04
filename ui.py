from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI:
    # This creates an expectation that the input has to be a QuizBrain class
    def __init__(self, quiz: QuizBrain):
        """
        Initializes the UI with the given QuizBrain instance.
        Sets up the main window, buttons, score label, and canvas for displaying questions.
        """
        self.quiz = quiz
        
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # Buttons
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")
        self.right_button = Button(image=self.true_image, borderwidth=0, command=self.check_answer_true)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=self.false_image, borderwidth=0, command=self.check_answer_false)
        self.wrong_button.grid(row=2, column=1)
        
        # Score
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        
        # Canvas
        self.canvas = Canvas(bg="white", highlightthickness=0, height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, text="santi", font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR, width=280)
        
        # Fetch the first question
        self.get_next_question()
        
        # Start the main event loop
        self.window.mainloop()

    def get_next_question(self):
        """
        Fetches the next question from the QuizBrain instance.
        Updates the canvas with the new question or displays a message if the quiz is finished.
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You finished the stack")
            self.right_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)

    def check_answer_true(self):
        """
        Checks if the answer 'True' is correct and updates the UI accordingly.
        """
        is_right = self.quiz.check_answer("True")
        self.check_answer(is_right)

    def check_answer_false(self):
        """
        Checks if the answer 'False' is correct and updates the UI accordingly.
        """
        is_right = self.quiz.check_answer("False")
        self.check_answer(is_right)

    def turn_white(self):
        """
        Resets the canvas background color to white and fetches the next question.
        """
        self.canvas.config(bg="white")
        self.get_next_question()

    def check_answer(self, is_right):
        """
        Updates the score and the UI based on whether the answer was correct.
        Changes the canvas background color to green for correct answers and red for incorrect ones.
        """
        if is_right:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.turn_white)

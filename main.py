from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

# Create a list of Question objects from the question data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the QuizBrain and UI
quiz = QuizBrain(question_bank)
quiz_ui = ui.UI(quiz)

# This part of the code is commented out as the UI handles the quiz progression
# while quiz.still_has_questions():
#     quiz.next_question()

# Print the final score once the quiz is complete
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# Declaring type variables
# age: int, name: str, height: float
# This indicates that the variables are expected to be of specific data types

# To specify the expected return type of a function, we can use the following syntax:
# def function_name() -> expected_return_type:

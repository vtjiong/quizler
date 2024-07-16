from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui=ui.UI(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# Declaring type variables
# age: int, name: str, height: float, what this is saying is that it expects an int or a string
# To tell what  a fucntion should expect the answer's data type should be we cna write def function name ()->
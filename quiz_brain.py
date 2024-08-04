import html


class QuizBrain:

    def __init__(self, q_list):
        """
        Initializes the QuizBrain object.

        Parameters:
        q_list (list): List of Question objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Checks if there are still questions left in the quiz.

        Returns:
        bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Fetches the next question from the question list, increments the question number,
        and returns the question text.

        Returns:
        str: The current question formatted as a string.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct and updates the score.

        Parameters:
        user_answer (str): The user's answer to the current question.

        Returns:
        bool: True if the user's answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return True
        else:
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return False

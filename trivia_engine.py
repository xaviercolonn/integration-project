import html
class TriviaEngine:

    # Instantiate the engine
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.q_number = 0
        self.current = None

    # Returns the next question in our questions list
    def get_next_question(self):
        self.current = self.questions[self.q_number]
        self.q_number += 1
        question_text = html.unescape(self.current.question)
        return f'Question {self.q_number}: {question_text}'

    # Check if the anser is correct and increments the score
    def check_answer(self, user_ans):
        if user_ans.lower() == self.current.answer.lower():
            self.score += 1
            return True
        return False
    # Returns True if there are remaining questions
    def rem_questions(self):
        return self.q_number < len(self.questions)

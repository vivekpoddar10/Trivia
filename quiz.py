import html

class Quiz:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        # fetch Question object stored at question_number position in the list
        self.current_question = self.question_bank[self.question_number]
        self.question_number += 1
        # ask the user
        q_text = html.unescape(self.current_question.question)
        return f"Q.{self.question_number}: {q_text}"


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False

import requests
from question import Question
from quiz import Quiz
from ui import QuizInterface

PARAMETER = {
    'amount': 10,
    'type': 'boolean'
}

def get_question_list():
    response = requests.get(url='https://opentdb.com/api.php', params=PARAMETER)
    response.raise_for_status()
    return response.json()['results']

question_list = get_question_list()

def create_question_bank():
    question_bank = []
    for item in question_list:
        # fetch question and answer from each object
        question = item['question']
        answer = item['correct_answer']
        # create a new Question object and append it to a list
        question_bank.append(Question(question, answer))
    return question_bank

quiz = Quiz(create_question_bank())
quiz_ui = QuizInterface(quiz)





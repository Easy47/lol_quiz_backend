import json
import random

QUIZZES_PATH="./quizzes/"
QUIZZES_JSON_FILENAME="quizzes.json"
QUESTIONS_JSON_FILENAME="questions.json"
NB_QUEST_PER_QUIZZ=15

def get_quizzes():

    d=''
    with open(QUIZZES_PATH+QUIZZES_JSON_FILENAME, 'r') as f:
        d=json.load(f)
    return list(d.values())


def get_quizz(id):

    quizzes=None
    with open(QUIZZES_PATH+QUIZZES_JSON_FILENAME, 'r') as f:
        quizzes=json.load(f)
    questions=None
    with open(QUIZZES_PATH + QUESTIONS_JSON_FILENAME, 'r') as f:
        questions=json.load(f)
    return [questions[(question_id)] for question_id in quizzes[(id)]["questions"]]

def create_random_quizz(difficulty):
    questions=None
    with open(QUIZZES_PATH + QUESTIONS_JSON_FILENAME, 'r') as f:
        questions=list(json.load(f).values())
    lg=len(questions)
    print(lg)
    rints=[]
    quizz_questions=[]
    while (len(rints) < 15):
        rint=random.randint(0, lg - 1)
        if (not rint in rints):
            quizz_questions.append(questions[rint])
            rints.append(rint)
    return quizz_questions

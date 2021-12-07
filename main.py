from question_model import Question
from quiz_brain import QuizBrain
from data import *
from logo import logo
import random
import urllib.request
import json
import os
import html


def clear(): os.system('cls' if os.name == 'nt' else 'clear')


def choose_category():
    print(logo)
    while True:
        difficulty = input("Choose difficult (easy/medium/hard):").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            break
        else:
            print("Wrong syntax! input again")
    print("Category for the question:")
    for number in question_category:
        print(f"{number}: {question_category[number]}")
    category = int(input("What do you want to choose: "))
    sl = 20
    while(True):
        url_link = "https://opentdb.com/api.php?amount="+ str(sl) + "&category=" + str(category + 8) + "&difficulty=" + difficulty
        data = json.loads(urllib.request.urlopen(url_link).read().decode())
        if data["response_code"] == 1:
            sl -= 1
        else:
            for i in range(len(data["results"])):
                data["results"][i]["question"] = html.unescape(data["results"][i]["question"])
            return data["results"]


quest_bank = []
question_data = choose_category()
for quest in question_data:
    quest_bank.append(Question(quest["type"], quest["question"], quest["correct_answer"], quest["incorrect_answers"]))
random.shuffle(quest_bank)

clear()
quiz = QuizBrain(quest_bank)

while quiz.is_still_have_quest():
    quiz.next_question()
quiz.final_score()

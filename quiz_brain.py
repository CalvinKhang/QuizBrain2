import random


class QuizBrain:

    def __init__(self, quest_list):
        self.quest_number = 0
        self.quest_list = quest_list
        self.score = 0

    def make_multi_choose(self, answer, incorrect_answers):
        a = []
        a.append(answer)
        for ans in incorrect_answers:
            a.append(ans)
        random.shuffle(a)
        options = {
            "A": a[0],
            "B": a[1],
            "C": a[2],
            "D": a[3]
        }
        return options

    def print_quest(self, quest):
        if quest.type == "multiple":
            option = self.make_multi_choose(quest.answer, quest.incorrect_answer)
            print(f"Q{self.quest_number + 1}: {quest.text}\n"
                  f"\tA) {option['A']}\n\tB) {option['B']}\n"
                  f"\tC) {option['C']}\n\tD) {option['D']}\t ")
            while (True):
                answer = input("Choose (A/B/C/D): ").upper()
                if answer not in ["A", "B", "C", "D"]:
                    print("You need to choose answer is A or B or C. => Choose agian")
                else:
                    break
            self.check_answer(option[answer], quest.answer)
        else:
            print(f"Q{self.quest_number + 1}: {quest.text}")
            answer = input("\tChoose (True/False): ").lower()
            self.check_answer(answer, quest.answer)

    def next_question(self):
        current_q = self.quest_list[self.quest_number]
        self.print_quest(current_q)
        print(f"Your current score is {self.score}/{self.quest_number} \n")

    def check_answer(self, answer, curren_q_answer):
        if answer.lower() == curren_q_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"the correct answer is {curren_q_answer}")
        self.quest_number += 1

    def final_score(self):
        print(f"Your final score is {self.score}/{self.quest_number}")

    def is_still_have_quest(self):
        return self.quest_number != len(self.quest_list)

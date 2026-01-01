from data import question_data
from question_model import ques
from quiz_brain import brain

ques_bank = []

for i in question_data:
    data = i["text"]
    answer = i["answer"]
    new_ques = ques(data,answer)
    ques_bank.append(new_ques)


quiz = brain(ques_bank)

while quiz.still_ques():
    if quiz.nxt() is False:
        break
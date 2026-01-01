from data import question_data
class brain :
    
    def __init__(self,lis):
        self.number = 0
        self.ques_list  = lis
        self.score = 0
        
    def still_ques(self):
        return len(self.ques_list) > self.number

        
    def nxt(self):
        curr_ques = self.ques_list[self.number]
        self.number += 1
        a = input(f"Q.{self.number}. {curr_ques.question}. (True/False)?: ")
        return self.check(a,curr_ques.answer,curr_ques)
        
        
    def check(self, answer1, answer2, correct_ans):
        
        if answer1.lower() == "stop":
            print("\nQuiz exited by user.\n")
            return False 
        if answer1.lower() == answer2.lower():
            self.score += 1
            print(f"\nYou are right ")
        else:
            print("\n Wrong Answer")
        print("\nCorrect answer is :",correct_ans.answer)
        print(f"\nYour Score is {self.score}/{self.number}\n")
            
        
        
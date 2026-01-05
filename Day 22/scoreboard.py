from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,250)

    def left_plus(self):
        self.score_left += 1
        self.clear()
        self.write(f"Your Score is : {self.score_left} / {self.score_right}", align="center", font=("arial",26,"bold"))
        
    def right_plus(self):
        self.score_right += 1
        self.clear()
        self.write(f"Your Score is : {self.score_left} / {self.score_right}", align="center", font=("arial",26,"bold"))
        
        
        
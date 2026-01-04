from turtle import Turtle

score = 0

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.score = 0
        self.show()
        
    def update(self):
        self.score += 1
        self.clear()
        self.show()
    
    def show(self):
        self.write(f"Your Score Is: {self.score}",align="center",font="arial")
        
    def end_show(self):
        self.goto(0,250)
        self.write(f"Your Score Is: {self.score}",align="center",font=("arial",26,"bold"))

    def end_game_animation(self):
        self.goto(0,0)
        self.clear()
        self.write(f"********GAME IS OVER********",align="center",font=("arial",24,"bold"))
        
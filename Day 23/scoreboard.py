from turtle import Turtle

score = 0

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.draw()
        

    def final(self):
        self.goto(0,100)
        self.write(f" GAME OVER ", align="center", font=("Courier", 45, "normal"))
        self.goto(0,0)
        self.write(f"Your Final Score is : {score}", align="center", font=("Courier", 35, "normal"))
        
    def rang_white(self):
        self.color("white")
        
    def rang_black(self):
        self.color("black")
        
    def draw(self):
        self.clear()
        self.goto(-180, 270)
        self.write(f"Score : {score}", align="center", font=("Courier", 25, "normal"))
        
        
    def increase(self):
        global score
        score += 1
        self.clear()
        self.draw()

from turtle import Turtle
import time


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xcord = 10
        self.ycord = 10
        self.factor = 1
        
    def move(self):
        self.goto(
            self.xcor()+self.xcord*self.factor,
            self.ycor()+self.ycord*self.factor
        )
    
    def bounce(self):
        self.ycord *= -1
    
    def bounce_by_paddle(self):
        self.factor += 0.1
        self.xcord *= -1
        
    def refresh(self):
        self.factor = 1
        self.goto(0,0)
        self.xcord *= -1
            
       
            

            
        
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.left(90)
        self.refresh()
        
        
    def refresh(self):
        self.goto(STARTING_POSITION)
        
    
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
    def check(self):
        if self.ycor() > 280:
            return True
        else:
            return False
        
        
        
        
    

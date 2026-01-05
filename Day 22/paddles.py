from turtle import Turtle




class Paddle(Turtle):
    
    def __init__(self,left_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(left_x,0)
        self.shapesize(stretch_wid=5,stretch_len=0.5)
        
    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
            
    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)
    
        
        
            

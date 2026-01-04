from turtle import Turtle,Screen,colormode
import random
from food1 import Food


X = 0
Y = 0
initial = 3
DIS = 20




class Snake:
    
    def __init__(self):
    
        self.snake_body = []
        self.create_snake()
        self.head  = self.snake_body[0] 
            
    def add(self):
        self.tail = self.snake_body[-1]
        tom = Turtle(shape="square")
        tom.color("white")
        tom.penup()
        tom.goto(self.tail.position())
        self.snake_body.append(tom)

    def corner_collision(self):
        x_low = -300
        x_high = 300
        y_low = -300
        y_high = 300
        x_verify = False
        y_verify = False
        
        if self.head.xcor() > x_low and self.head.xcor() < x_high:
            x_verify = True
        if self.head.ycor() > y_low and self.head.ycor() < y_high:
            y_verify = True
        else:
            return
        
        if x_verify and y_verify:
            return False
        else:
            return True
        
                        
    def check_body_collision(self):
        for i in range(1,len(self.snake_body)):
            if self.head.distance(self.snake_body[i])  < 10:
                return True
        return False
            
    

    def create_snake(self):
        for i in range(0,initial):
            tom = Turtle(shape="square")
            tom.color("white")
            tom.penup()
            tom.goto(X-i*20,Y)
            tom.speed(0.5)
            self.snake_body.append(tom)
        

    def move(self):
        for i in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x,new_y)
        self.snake_body[0].forward(DIS)
        
    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)
        
    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
        
    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
        
    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
        

    

















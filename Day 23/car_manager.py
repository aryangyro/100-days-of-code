from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
staring = 5
incriment = 1

class CarManager():
    
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        
        chance = random.randint(1,6)
        if chance == 1:
            tom = Turtle(shape="square")
            tom.color(random.choice(COLORS))
            tom.penup()
            tom.shapesize(stretch_len=2,stretch_wid=1)
            tom.goto(300,random.randint(-220,250))
            self.all_cars.append(tom)
        
    def move_car(self):
        for car in self.all_cars:
            a = car.xcor() - staring
            car.goto(a,car.ycor())
    
    def icrease_speed(self):
        global staring
        global incriment
        staring += incriment
            
        
    
            
    
        
        
    

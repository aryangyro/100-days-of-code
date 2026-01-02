from turtle import Turtle,Screen,colormode
import random
Screen = Screen()
colormode(255)
tom = Turtle()
tom.pensize(5)

def move():
    tom.forward(10)
    
def left_angle():
    tom.left(10)    

def right_angle():
    tom.right(10)

def back():
    tom.backward(10)

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tom.pencolor(r,g,b)
def clr():
    tom.clear()    
    tom.penup()
    tom.goto(0,0)
    tom.pendown()
    tom.setheading(0)

Screen.listen()
Screen.onkey(move,"w")
Screen.onkey(left_angle,"a")
Screen.onkey(right_angle,"d")
Screen.onkey(right_angle,"s")
Screen.onkey(change_color,"space")
Screen.onkey(clr,"c")



Screen.exitonclick()
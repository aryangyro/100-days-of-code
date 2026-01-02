import random
from turtle import Turtle,Screen,colormode

tom = Turtle()
tom.shape("turtle")
tom.color("black")
tom.speed(0)
# tom.pensize(5)
colormode(255)

def colorchange():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tom.pencolor(r,g,b)

# a = 0
# while a < 1000:
#     ls = [0,90,180,270]
#     Choice = random.choice(ls)
#     tom.forward(10)
#     a += 10
#     tom.left(Choice)
#     colorchange()

def spirograph (a):
    loop = 0
    
    while loop != a:
        tom.circle(50)
        tom.left(360/a)
        loop += 1
        colorchange()

spirograph(50)

tom.hideturtle()
    



skreen = Screen()
skreen.exitonclick()


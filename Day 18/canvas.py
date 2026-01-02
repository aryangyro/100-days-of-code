from turtle import Turtle, Screen, colormode
import random

colormode(255)

tom = Turtle()
tom.hideturtle()
tom.speed("fastest")
tom.penup()

def colorchange():
    tom.pencolor(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )

start_x = -200
start_y = -200

tom.goto(start_x, start_y)

y = start_y

while y <= 200:
    x = start_x
    tom.goto(x, y)

    while x <= 200:
        colorchange()
        tom.dot(10)
        tom.forward(20)
        x += 20

    y += 20

screen = Screen()
screen.exitonclick()
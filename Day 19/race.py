from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)

colors = ["red", "green", "blue", "pink", "black"]
turtles = []


start_x = -300
start_y = 200

for i in range(5):
    t = Turtle("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(start_x, start_y - i * 60)
    turtles.append(t)

a = input("On which Tutle you wanna bet on: ")

line = Turtle()
line.penup()
line.goto(300, 250)
line.pendown()
line.goto(300, -150)
line.hideturtle()

race_on = True

def move():
    global race_on
    global a

    for t in turtles:
        if t.xcor() >= 300:
            race_on = False
            
            if t.pencolor()[0] != a:
                print("You Lost The Bet")
            else:
                print("You Won the bet")
                
            print(f"{t.pencolor()} turtle wins!")
            return

        t.forward(random.randint(1, 6))

    if race_on:
        screen.ontimer(move, 50)   

move()

screen.exitonclick()
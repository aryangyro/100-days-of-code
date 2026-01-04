from turtle import Turtle,Screen,colormode
import random
import time
from snakey import Snake

screen = Screen()
screen.title("Sanke Game Is Here",)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    



screen.exitonclick()
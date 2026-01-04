from turtle import Turtle,Screen,colormode
import random
import time
from snakey1 import Snake
import food1
import scoreboard
screen = Screen()
screen.title("Sanke Game Is Here",)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = food1.Food()
score = scoreboard.Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    
    if snake.head.distance(food) < 20:
        score.update()
        snake.add()
        food.refresh()
    
    

    snake.move()
    

    if snake.check_body_collision():
        game_on = False
        screen.clearscreen()
        screen.bgcolor("black")
        score.end_game_animation()
        score.end_show()
    
    if snake.corner_collision():
        game_on = False
        screen.clearscreen()
        screen.bgcolor("black")
        score.end_game_animation()
        score.end_show()
        
        



screen.exitonclick()
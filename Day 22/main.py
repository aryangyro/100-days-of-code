from turtle import Turtle,Screen,colormode
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Score

Screen = Screen()
Screen.setup(height=600,width=800)
Screen.bgcolor("black")
Screen.title("Ping Pong Game")
# Screen.delay(0.001)
Screen.tracer(0)

left_paddle = Paddle(-380)
right_paddle = Paddle(380)
ball = Ball()
score = Score()

def game_off():
    global game_on
    game_on = False

Screen.listen()
Screen.onkey(left_paddle.move_up,"w")
Screen.onkey(left_paddle.move_down,"s")
Screen.onkey(right_paddle.move_up,"Up")
Screen.onkey(right_paddle.move_down,"Down")
Screen.onkey(game_off, "y")
game_on = True



while game_on:
    time.sleep(0.1)
    Screen.update()
    ball.move()
    
    
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()
        
    if ball.xcor() > 360 and ball.xcord > 0:
        if ball.distance(right_paddle) < 40:
            ball.bounce_by_paddle()
            continue
        else:
            score.left_plus()
            ball.refresh()
    
    elif ball.xcor() < -360 and ball.xcord < 0:
        if ball.distance(left_paddle) < 40:
            ball.bounce_by_paddle()
            continue
        else:
            score.right_plus()
            ball.refresh()

            
    




Screen.exitonclick()


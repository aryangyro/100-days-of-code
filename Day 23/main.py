import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finish_line import Finish_line

back = "black"
back2 = "white"
final_color = back


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross Game")
screen.bgcolor(final_color)
screen.tracer(0)

def colorchange():
    global final_color
    
    if not game_is_on:
        return
    
    elif final_color == back:
        final_color = back2
        screen.bgcolor(final_color)
        player.color("black")
        finish_line.rang_black()
        scoreboard.rang_black()
    else:
        final_color = back
        screen.bgcolor(final_color)
        player.color("white")
        finish_line.rang_white()
        scoreboard.rang_white()
    scoreboard.draw()

player = Player()
screen.listen()
screen.onkey(player.move,"w")
screen.onkey(colorchange,"l")
carManager = CarManager()
scoreboard = Scoreboard()

finish_line = Finish_line()
finish_line.rang_white()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move_car()
    
    if player.check():
        carManager.icrease_speed()
        scoreboard.increase()
        player.refresh()
        
    collision = False
    
    for car in carManager.all_cars:
        if car.distance(player) < 25:
            collision = True
            break
    
    if collision:
        game_is_on = False
        for car in carManager.all_cars:
            car.hideturtle()
        player.hideturtle()
        scoreboard.hideturtle()
        finish_line.clear()
        finish_line.hideturtle()
        scoreboard.clear()
        scoreboard.final()
        screen.update()
    
    
    
screen.exitonclick()

# Snake-Game:

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

sap = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(sap.up, 'Up')
screen.onkey(sap.down, 'Down')
screen.onkey(sap.left, 'Left')
screen.onkey(sap.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    sap.move()
    
    # Detect collision with food:
    if sap.head.distance(food) < 22:
        score.increase_score()
        sap.extend()
        food.refresh()
    
    # Detect collision with wall:
    if sap.head.xcor() > 290 or sap.head.xcor() < -290 or sap.head.ycor() > 250 or sap.head.ycor() < -290:
        game_is_on = False
        screen.clearscreen()
        screen.bgcolor('black')
        score.gameover()
        
    # Detect collision with tail:
    for segment in sap.segments[1:]:
        if sap.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()
    
    
screen.exitonclick()
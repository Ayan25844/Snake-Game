end=False
import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard

screen=Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")

food=Food()
snake=Snake()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while(not end):
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.count+=1
        snake.extend()
        scoreboard.score+=1
        scoreboard.update_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        end=True
        scoreboard.over()
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            end=True
            scoreboard.over()

screen.exitonclick()
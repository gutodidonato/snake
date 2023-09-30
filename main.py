from turtle import *
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
game_is_on = True
screen.tracer(0)

def game_lose():
    if (snake.corpo[0].xcor() > 300) or (snake.corpo[0].xcor() < -300) or (snake.corpo[0].ycor() > 300) or (snake.corpo[0].ycor() < -300):
        return False
    elif snake.morder_corpo() == "mordeu":
        return False
    else:
        return True
    

    
while game_lose():
    screen.update()
    time.sleep(0.1)
    snake.move()
    


screen.exitonclick()

        
    
        
    
    





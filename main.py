from turtle import *
from snake import Snake
from point import Point
from nota import Nota
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
pontos = Nota()
snake = Snake()
food = Point()

screen.listen()
screen.onkey(snake.cima, "Up")
screen.onkey(snake.baixo, "Down")
screen.onkey(snake.esquerda, "Left")
screen.onkey(snake.direita, "Right")


game_is_on = True
screen.tracer(0)


def colisao_comida():
    if snake.corpo[0].distance(food) < 15:
        print("nom nom")
        food.fui_comido()
        pontos.make_point()

def game_lose():
    if (snake.corpo[0].xcor() > 280) or (snake.corpo[0].xcor() < -280) or (snake.corpo[0].ycor() > 280) or (snake.corpo[0].ycor() < -280):
        pontos.fim_de_jogo()
        return False
    elif snake.morder_corpo() == "mordeu":
        pontos.fim_de_jogo()
        return False
    else:
        return True
    

    
while game_lose():
    screen.update()
    time.sleep(0.1)
    snake.move()
    colisao_comida()
    
    


screen.exitonclick()
from turtle import *
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

corpo_inicial = [(0, 0), (-20, 0), (-40, 0)]
corpo =[]
game_is_on = True
screen.tracer(0)

def esquerda():
    corpo[0].left(90)
def direita():
    corpo[0].right(90)

for posicao in corpo_inicial:
    segmento = Turtle("square")
    segmento.color("white")
    segmento.penup()
    segmento.goto(posicao)
    corpo.append(segmento)
    
while game_is_on:
    screen.update()
    time.sleep(1)
    for segmento in range(len(corpo) -1 ,0, -1):
        '''de trás para frente'''
        posicao_x_nova = corpo[segmento - 1].xcor()
        posicao_y_nova = corpo[segmento - 1].ycor()
        corpo[segmento].goto(posicao_x_nova, posicao_y_nova)
    corpo[0].forward(20)
    direita()
    '''
    libera a restrição de ter que loopar cada um de uma vez, pq considera a movimentação dos segmentos anteriores
    '''
    


screen.exitonclick()

        
    
        
    
    





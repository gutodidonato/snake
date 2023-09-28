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


for posicao in corpo_inicial:
    segmento = Turtle("square")
    segmento.color("white")
    segmento.penup()
    segmento.goto(posicao)
    corpo.append(segmento)
    
estado = "frente"

def mover():
    
            
            
            
                
            
            
        
mover()
 
 


screen.exitonclick()

        
    
        
    
    





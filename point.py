from turtle import *
import random 

class Point:
    def __init__ (self):
        pass
    
    def gerar_corpo(self):
        ponto = Turtle("square")
        ponto.color("white")
        self.corx(random.randint(-300, 300))
        self.cory(random.randint(-300, 300))
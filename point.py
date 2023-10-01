from turtle import *
import random 

class Point(Turtle):
    
    
    def __init__(self):
        super().__init__
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        random_x = random.randint(-300, 300)
        random_y = random.randint(-300, 300)
        self.goto(random_x, random_y)
    
    def gerar_corpo(self):
        ponto = Turtle("square")
        ponto.color("white")
        self.corx(random.randint(-300, 300))
        self.cory(random.randint(-300, 300))
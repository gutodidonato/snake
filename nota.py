from turtle import *

class Nota(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write(f"Pontos: {self.score}", align="center", font=("Arial", 22, "normal"))
        self.hideturtle()

    def atualizar_score(self):
        self.write(f"Pontos: {self.score}", align="center", font=("Arial", 22, "normal"))
        
    def make_point(self):
        self.score += 1
        self.clear()
        self.atualizar_score()
        
    def fim_de_jogo(self):
        self.goto(0,0)
        self.write(f"FIM DE JOGO!", align="center", font=("Arial", 22, "normal"))

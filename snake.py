from turtle import *
MOVE_DISTANCE = 20
POSICOES_INICIAIS = [(0, 0), (-20, 0), (-40, 0)]



class Snake:
        
    
    def __init__(self):
        self.corpo =[]
        self.corpo_inicial = [(0, 0), (-20, 0), (-40, 0)]
        self.criar_cobra()
        
    def criar_cobra(self):
        for posicao in self.corpo_inicial:
            segmento = Turtle("square")
            segmento.color("white")
            segmento.penup()
            segmento.goto(posicao)
            self.corpo.append(segmento)
            
    def morder_corpo(self):
        for parte in self.corpo[1:]:
            if parte.xcor() == self.corpo[0].xcor() and parte.ycor() == self.corpo[0].ycor():
                return "mordeu"
            
    def move(self):
        for segmento in range(len(self.corpo) -1 ,0, -1):
            '''de trás para frente'''
            posicao_x_nova = self.corpo[segmento - 1].xcor()
            posicao_y_nova = self.corpo[segmento - 1].ycor()
            self.corpo[segmento].goto(posicao_x_nova, posicao_y_nova)
        self.corpo[0].forward(MOVE_DISTANCE)
    '''
    libera a restrição de ter que loopar cada um de uma vez, pq considera a movimentação dos segmentos anteriores
    '''
    def esquerda(self):
        self.corpo[0].setheading(180)
    def direita(self):
        self.corpo[0].setheading(0)
    def cima(self):
        self.corpo[0].setheading(90)
    def baixo(self):
        self.corpo[0].setheading(270)
        
        
from turtle import *
MOVE_DISTANCE = 20
POSICOES_INICIAIS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:   
    
    def __init__(self):
        self.corpo =[]
        self.corpo_inicial = POSICOES_INICIAIS
        self.criar_cobra()
        self.state = "right"
        
    def criar_cobra(self):
        for posicao in self.corpo_inicial:
            self.crescer(posicao)
            
            
    def crescer(self, posicao):
        segmento = Turtle("square")
        segmento.color("white")
        segmento.penup()
        segmento.goto(posicao)
        self.corpo.append(segmento)
        
    def crescer_alimentar(self):
        self.crescer(self.corpo[-1].position())
        
    def morder_corpo(self):
        #utilizei o slice em python
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
        if self.state == "right":
            pass
        else:
            self.corpo[0].setheading(LEFT)
            self.state = "left"
    def direita(self):
        if self.state == "left":
            pass
        else:
            self.corpo[0].setheading(RIGHT)
            self.state = "right"
    def cima(self):
        if self.state == "down":
            pass
        else:
            self.corpo[0].setheading(UP)
            self.state = "up"
    def baixo(self):
        if self.state == "up":
            pass
        else:
            self.corpo[0].setheading(DOWN)
            self.state = "down"
        
        
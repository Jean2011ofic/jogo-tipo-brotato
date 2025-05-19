import pygame
class Projeteis:
    def __init__(self, x_p ,y_p ,quantidade , velocidade,dano,dono, tela):
        self.x_p = x_p
        self.y_p = y_p
        self.quantidade = quantidade
        self.velocidade = velocidade
        self.dano = dano
        self.p_rect : pygame.rect
        self.direcao_x = None
        self.direcao_y = None
        self.tela = tela


    def desenhar(self):
        self.p_rect = pygame.draw.rect(self.tela,(255,100,100),(self.x_p, self.y_p, 10,10))
    
    def calcula_atirar(self):
        x_m,y_m = pygame.mouse.get_pos()
        delta_x = x_m - self.x_p 
        delta_y = y_m - self.y_p  
        distancia = (delta_x ** 2 + delta_y ** 2) ** 0.5

        self.direcao_x = delta_x / distancia
        self.direcao_y = delta_y / distancia


    def atualiza(self):
            self.x_p += self.direcao_x * self.velocidade
            self.y_p += self.direcao_y * self.velocidade
            self.desenhar()

    def atira(self):
        self.calcula_atirar()
        self.atualiza()



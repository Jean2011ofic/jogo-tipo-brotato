import pygame

from projeteis import Projeteis
from gerenciador_p import Gerenciador_P
from gerenciador_pl import Gerenciador_Pl



class Inimigo:
    def __init__(self , tela):
        self.x = 50
        self.y = 50
        self.rect = None
        
        self.velocidade = 10
        self.dano = 1
        self.vida = 10
        self.atqs = 1

        self.tela = tela
        self.recompensa_dinheiro = 10

        self.g_pl = Gerenciador_Pl()
        self.player = self.g_pl.pegar_player()
        while self.player == None:
            self.player = self.g_pl.pegar_player()


    def desenhar(self):

        self.rect = pygame.draw.rect(self.tela,(255,0,0),(self.x,self.y, 50,50))
    def calcula_alvo(self):
        print(self.player.__class__)
        x_m, y_m = self.player.player_rect.x, self.player.player_rect.y
        delta_x = x_m - self.x
        delta_y = y_m - self.y  
        distancia = (delta_x ** 2 + delta_y ** 2) ** 0.5

        self.direcao_x = delta_x / distancia
        self.direcao_y = delta_y / distancia
    def ir_ate_player(self):
        self.x += self.direcao_x * self.velocidade
        self.y += self.direcao_y * self.velocidade

    
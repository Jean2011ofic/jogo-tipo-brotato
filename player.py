import pygame

from projeteis import Projeteis
from gerenciador_p import Gerenciador_P


class Player:
    def __init__(self, cor, x_player, y_player, tela):
        self.cor = cor
        self.x_player = x_player
        self.y_player = y_player

        self.player_rect = None
        self.largula = 50
        self.altura = 50

        # atributos vida
        self.vida_maxima = 10
        self.vida = self.vida_maxima
        self.regeneraçao = 0

        self.velocidade = 10

        self.g_p = Gerenciador_P(tela)

        self.tela = tela

        self.projeteis = []

        self.dinheiro = 0


    def desenhar(self):
        self.player_rect = pygame.draw.rect(self.tela, self.cor, (self.x_player, self.y_player, self.altura, self.largula))

    
    def movimentacao(self,evento):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]: 
            self.y_player -= self.velocidade
        if teclas[pygame.K_s]: 
            self.y_player += self.velocidade
        if teclas[pygame.K_a]:  
            self.x_player -= self.velocidade
        if teclas[pygame.K_d]:  
            self.x_player += self.velocidade
        if evento.type == pygame.MOUSEBUTTONDOWN:
            projetil = Projeteis(self.x_player,self.y_player,1,20,1,"player",self.tela)
            projetil.desenhar()
            projetil.atira()
            self.g_p.registrar_projeteis(projetil)
    def dar_dinheiro(self, quantidade):
        self.dinheiro += quantidade

        

        
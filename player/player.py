import pygame

from projeteis.projeteis import Projeteis
from projeteis.gerenciador_p import Gerenciador_P

import pygame
from projeteis.projeteis import Projeteis
from projeteis.gerenciador_p import Gerenciador_P
from cooldown import Cooldown  # Certifique-se de que a classe tem um nome correto

class Player:
    def __init__(self, cor, x_player, y_player, tela):
        self.cor = cor
        self.x_player = x_player
        self.y_player = y_player

        self.largura = 50
        self.altura = 50

        self.player_rect = pygame.Rect(self.x_player, self.y_player, self.altura, self.largura)

        # Atributos vida
        self.vida_maxima = 10
        self.vida = self.vida_maxima
        self.regeneracao = 0

        self.velocidade = 10
        self.g_p = Gerenciador_P(tela)
        self.tela = tela
        self.projeteis = []
        self.dinheiro = 0
        self.atqps = 2

        # Cooldown do tiro
        self.c_t = Cooldown()
        self.c_t.entrar_c((1 / self.atqps) * 1000)  # Correção: agora chamamos o método corretamente

    def desenhar(self):
        self.player_rect = pygame.draw.rect(self.tela, self.cor, (self.x_player, self.y_player, self.altura, self.largura))

    def movimentacao(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]: 
            self.y_player -= self.velocidade
        if teclas[pygame.K_s]: 
            self.y_player += self.velocidade
        if teclas[pygame.K_a]:  
            self.x_player -= self.velocidade
        if teclas[pygame.K_d]:  
            self.x_player += self.velocidade

        # Adicionando cooldown ao disparo do projétil
        if pygame.mouse.get_pressed()[0]:  
            if self.c_t.verificar():  # Só dispara se o cooldown permitir
                projetil = Projeteis(self.x_player, self.y_player, 1, 20, 1, "player", self.tela)
                projetil.desenhar()
                projetil.atira()
                self.g_p.registrar_projeteis(projetil)
                self.c_t.entrar_c((1 / self.atqps) * 1000)  # Reinicia o cooldown corretamente após cada tiro

    def atualizar_player(self):
        self.desenhar()
        self.movimentacao()


    def dar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
import pygame

# from projeteis.projeteis import Projeteis
from player.gerenciador_pl import Gerenciador_Pl



class Inimigo:
    def __init__(self , tela):
        print("criando inimigo")
        self.x = 50
        self.y = 50
        self.rect = None
        
        self.velocidade = 10
        self.dano = 1
        self.vida = 2
        self.atqs = 1

        self.tela = tela
        self.recompensa_dinheiro = 10

        self.g_pl = Gerenciador_Pl(tela)

        self.player = self.g_pl.pegar_player()

    def desenhar(self):
        print("desenhando")
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
        self.calcula_alvo()
        self.x += self.direcao_x * self.velocidade
        self.y += self.direcao_y * self.velocidade
    
    def atualizar(self):
        self.ir_ate_player()
        self.desenhar()
    def verificar_morreu(self):
        if self.vida <= 0:
            print("inimigo morreu")
            return True
        return False
    def receber_dano(self, dano):
        print("recebendo dano")
        self.vida -= dano
        if self.verificar_morreu():
            return True
        return False
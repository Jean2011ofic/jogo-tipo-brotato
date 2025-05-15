import pygame
from gerenciador_p import Gerenciador_P

Player = None

inimigos = []

class Gerenciador_DMR:
    def __init__(self):
        self.Player = Player
        self.inimigo = inimigos

    def dar_recompensa(self,inimigo,player):
        recompensa_dinheiro = inimigo.recompensa_dinheiro
        self.Player.dar_dinheiro(recompensa_dinheiro)
    

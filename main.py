import pygame
import sys

from player.player import Player
from projeteis.projeteis import Projeteis
from projeteis.gerenciador_p import Gerenciador_P
from player.gerenciador_pl import Gerenciador_Pl
from inimigos.inimigo import Inimigo
from inimigos.gerenciador_ini import Gerenciador_ini

import time

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("jogo")

relogio = pygame.time.Clock()


g_p = Gerenciador_P(tela)
g_pl = Gerenciador_Pl(tela)
g_ini = Gerenciador_ini(tela)

player = g_pl.iniciar_player()
g_ini.criar_inimigo()

ini = Inimigo(tela)

while True:
    tela.fill((0,0,0))
    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
        



    

    g_pl.atualizar_player()
    g_p.atualizar()
    g_ini.atualizar_inimigos()
    pygame.display.flip()

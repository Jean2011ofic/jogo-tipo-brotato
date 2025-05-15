import pygame
import sys

from player import Player
from projeteis import Projeteis
from gerenciador_p import Gerenciador_P
from gerenciador_pl import Gerenciador_Pl

from inimigo import Inimigo

import time

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("jogo")

relogio = pygame.time.Clock()


g_p = Gerenciador_P(tela)

g_pl = Gerenciador_Pl()
player = g_pl.iniciar_player()

ini = Inimigo(tela)
ini.calcula_alvo()
while True:
    tela.fill((0,0,0))
    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    teste = pygame.draw.rect(tela,(0,0,0),(50,50,50,50))

    print(teste.x)
        
    g_p.atualizar()
    pygame.display.flip()

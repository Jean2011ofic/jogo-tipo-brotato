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

g_pl = Gerenciador_Pl(tela)
player = g_pl.iniciar_player()

ini = Inimigo(tela)

while True:
    tela.fill((0,0,0))
    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
        


    print(f"Posição do player: {g_pl.player.player_rect.x}, {g_pl.player.player_rect.y}")    
    

    g_pl.atualizar_player()
    ini.desenhar()
    ini.ir_ate_player()
    g_p.atualizar()
    pygame.display.flip()

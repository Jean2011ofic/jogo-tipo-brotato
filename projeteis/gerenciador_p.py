import pygame
from projeteis.projeteis import Projeteis
from combate_manager.CollisionManager import CollisionManager


projeteis_g = []

class Gerenciador_P:
    def __init__(self,tela):
        self.projeteis = projeteis_g
        self.tela = tela
        self.cm = CollisionManager()


    def criar_projetil(self,x_p ,y_p, quantidade , velocidade,dano,dono, tela):
        x = Projeteis(x_p ,y_p, quantidade , velocidade,dano,dono, tela)
        x.desenhar()
        x.atira()
        self.projeteis.append(x)
        self.cm.adicionar_ataque_a_verificacao(dono ,dano ,x.p_rect)



    def atualizar(self):
        for x in self.projeteis:
            if isinstance(x,Projeteis):
                x.atualiza()

            

    
    
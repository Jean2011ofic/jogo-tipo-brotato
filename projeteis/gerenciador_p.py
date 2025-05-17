import pygame
from projeteis.projeteis import Projeteis


projeteis_g = []

class Gerenciador_P:
    def __init__(self,tela):
        self.projeteis = projeteis_g
        self.tela = tela

    def registrar_projeteis(self, projeteis):
        self.projeteis.append(projeteis)
        #projeteis_g.append(projeteis)

    def atualizar(self):
        for x in self.projeteis:
            x.atualiza()

    # def verificar_acerto(self):
    #     for projetil in self.projeteis:
    #         if projetil.
            

    
    
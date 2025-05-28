import pygame

class Gerenciador_Dano:
    def __init__(self):
        self.tela = pygame.display.get_surface()
    
    def dar_dano(self, inimigo, dano):
        
        if inimigo.receber_dano(dano):
            self.remover_inimigo(inimigo)
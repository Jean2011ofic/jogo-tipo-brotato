import pygame

class Gerenciador_Dano:
    def __init__(self):
        self.tela = pygame.display.get_surface()
    
    def dar_dano(self, inimigo, dano):
        
        if hasattr(inimigo, 'vida'):
            inimigo.vida -= dano
            if inimigo.vida <= 0:
                print(f"Inimigo {inimigo} derrotado!")
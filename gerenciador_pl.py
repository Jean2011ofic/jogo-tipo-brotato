from player import Player
import pygame

class Gerenciador_Pl:   
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance            

    def __init__(self, n=None):
        self.player = None
        self.tela = pygame.display
        self.iniciado = False

    def iniciar_player(self):
        t = pygame.display.get_window_size()
        self.player = Player((255, 255, 255), t[0]//2, t[1]//2, self.tela)
        self.iniciado = True

    def pegar_player(self):
        if self.player is None:
            self.iniciar_player()
        return self.player
    
        
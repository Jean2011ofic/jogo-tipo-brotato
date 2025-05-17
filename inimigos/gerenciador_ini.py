import pygame
from inimigos.inimigo import Inimigo

class Gerenciador_ini:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance
    
    def __init__(self, tela):
        self.tela = tela
        self.inimigos = []

    def criar_inimigo(self):
        x = Inimigo(self.tela)
        x.desenhar()
        self.inimigos.append(x)
        print("inimigo criado e registrado")
    
    def atualizar_inimigos(self):
        for inimigo in self.inimigos:
            if isinstance(inimigo, Inimigo):
                inimigo.atualizar()
                print("atualizado")

        
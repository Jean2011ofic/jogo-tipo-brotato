import pygame
from inimigos.inimigo import Inimigo

class Gerenciador_ini:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("criando singleton")
        return cls._instance
    
    def __init__(self, tela):
        self.tela = tela
        if not hasattr(self, "inimigos"):  # Apenas se ainda não existir
            self.inimigos = []


    def criar_inimigo(self):
        x = Inimigo(self.tela)
        x.desenhar()
        self.inimigos.append(x)
    
    def atualizar_inimigos(self):
        for inimigo in self.inimigos:
            if isinstance(inimigo, Inimigo):
                inimigo.atualizar()

    
    def pegar_inimigos(self):
        return self.inimigos

        
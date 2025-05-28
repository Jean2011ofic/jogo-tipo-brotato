import pygame
from combate_manager.gerenciador_dano import Gerenciador_Dano


class CollisionManager:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        from inimigos.gerenciador_ini import Gerenciador_ini
        self.tela = pygame.display.get_surface()
        self.g_ini = Gerenciador_ini(self.tela)
        self.inimigos = self.g_ini.pegar_inimigos()
        print(self.inimigos)
        self.ataques_em_progresso = []
        self.gd = Gerenciador_Dano()

    def verificar_ataques(self):
        self.inimigos = self.g_ini.pegar_inimigos()
        print("verificando ataques")
        for ataque in self.ataques_em_progresso:           
            if ataque["tipo"] == "player":
                ar = ataque["rect"]
                if isinstance(ar, pygame.Rect):
                    print("verificando colisao com inimigos")
                    for inimigo in self.inimigos:
                        from inimigos.inimigo import Inimigo
                        if isinstance(inimigo, Inimigo):
                            print("verificando colisao com inimigo")
                            if ar.colliderect(inimigo.rect):
                                print("acertou inimigo")
                                if inimigo.receber_dano(ataque["dano"]):
                                    self.inimigos.remove(inimigo)
                                self.ataques_em_progresso.remove(ataque)

    def adicionar_ataque_a_verificacao(self,tipo,dano,rect):
        self.ataques_em_progresso.append({
            "tipo" : tipo,
            "dano" : dano,
            "rect" : rect
        })




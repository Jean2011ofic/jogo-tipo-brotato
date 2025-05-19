import pygame



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

    def verificar_ataques(self):
        for ataque in self.ataques_em_progresso:
            if ataque["tipo"] == "player":
                if isinstance(ataque["rect"], pygame.Rect):
                    for inimigo in self.inimigos:
                        if ataque["rect"].colliderect(inimigo.rect):
                            print("acertou inimigo")

    def adicionar_ataque_a_verificacao(self,tipo,dano,rect):
        self.ataques_em_progresso.append({
            "tipo" : tipo,
            "dano" : dano,
            "rect" : rect
        })




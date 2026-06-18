class Base:
    
    def __init__(self):
        self.vida = 500

    def recibir_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    def esta_destruida(self):
        return self.vida <= 0

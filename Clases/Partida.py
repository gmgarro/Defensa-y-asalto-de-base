from Mapa import Mapa
class Partida:
    
    def __init__(self):

        self.mapa = Mapa()
        self.ronda = 1
        
        self.dinero_defensor = 1000
        self.dinero_atacante = 1000
        
        self.jugador_defensor = None
        self.jugador_atacante = None
    
    def siguiente_ronda(self):
        self.ronda += 1
    
    def agregar_dinero_defensor(self, cantidad):
        self.dinero_defensor += cantidad

    def agregar_dinero_atacante(self, cantidad):
        self.dinero_atacante += cantidad
    
    def defensor_puede_comprar(self, costo):
        return self.dinero_defensor >= costo
    
    def atacante_puede_comprar(self, costo):
        return self.dinero_atacante >= costo
from Unidad import Unidad

class Soldado(Unidad):
    def __init__(self):
        super().__init__(
            nombre="Soldado",
            costo=50,
            vida=100,
            dano=20,
            velocidad=2,
            habilidad="Disparo doble",
            turnos_habilidad=3
        )
        
        self.disparo_doble = False
    
    def activar_habilidad(self, mapa):
        self.disparo_doble = True
    
    def atacar(self, unidad):
        super().atacar(unidad)

        if self.disparo_doble:
            super().atacar(unidad)
            self.disparo_doble = False